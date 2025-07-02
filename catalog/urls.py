from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import view_home, view_contact, detail_product

app_name = CatalogConfig.name

urlpatterns = [
    path("", view_home, name='home'),
    path("contacts/", view_contact, name='contacts'),
    path("detail_product/<int:pk>", detail_product, name='detail_product'),
]