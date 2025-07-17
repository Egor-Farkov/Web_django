from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    def get_success_url(self):
        return reverse_lazy("catalog:detail_product", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy("catalog:home")

