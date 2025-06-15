from django.shortcuts import render

# Create your views here.
def view_home(request):
    return render(request, template_name="home.html")


def view_contact(request):
    return render(request, template_name="contacts.html")
