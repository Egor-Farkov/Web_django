from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.defaults import permission_denied
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'



class ProductContactView(TemplateView):
    template_name = 'contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    def get_success_url(self):
        return reverse_lazy("catalog:detail_product", kwargs={"pk": self.object.pk})

    def get_form_class(self):
        product = self.object
        user = self.request.user
        if user != product.owner:
            return PermissionDenied
        if not user.has_perms('catalog.can_unpublish_product'):
            return PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy("catalog:home")
    permission_required = 'catalog.can_delete_product'

    def get_form_class(self):
        product = self.object
        user = self.request.user
        if user != product.owner:
            return PermissionDenied
        if not user.has_perms('catalog.can_delete_product'):
            return PermissionDenied

