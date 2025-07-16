from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductContactView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, \
    ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='home'),
    path("contacts/", ProductContactView.as_view(), name='contacts'),
    path("detail_product/<int:pk>", ProductDetailView.as_view(), name='detail_product'),
    path("update_product/<int:pk>", ProductUpdateView.as_view(), name='update_product'),
    path("delete_product/<int:pk>", ProductDeleteView.as_view(), name='delete_product'),
    path("create_product/", ProductCreateView.as_view(), name='create_product'),
]