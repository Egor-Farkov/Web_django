from catalog.models import Product


def get_products_from_category(id_category):
    return Product.objects.filter(category=id_category)