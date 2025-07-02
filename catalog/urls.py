from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductContactView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='home'),
    path("contacts/", ProductContactView.as_view(), name='contacts'),
    path("detail_product/<int:pk>", ProductDetailView.as_view(), name='detail_product'),
]