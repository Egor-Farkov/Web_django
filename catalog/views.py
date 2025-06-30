from django.shortcuts import render


from catalog.models import Product


# Create your views here.

def view_home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name="home.html", context=context)


def view_contact(request):
    return render(request, template_name="contacts.html")


def detail_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, template_name="detail_product.html", context=context)
