from django.urls import path

from catalog.views import view_home, view_contact

urlpatterns = [
    path("", view_home),
    path("home/", view_home),
    path("contacts/", view_contact),
]