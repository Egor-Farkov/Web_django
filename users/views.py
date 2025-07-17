import secrets
from gc import get_objects

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.models import CustomUser


# Create your views here.
# Форма регистрации
class CustomUserCreationForm(CreateView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = '__all__'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()
        address = self.request.get_host()
        url = f'http://{address}/user/valid_token/{user.token}'
        print(url)
        send_mail(subject='Подтвердите email', message=f'Перейдите по ссылке {url}',
                  from_email=EMAIL_HOST_USER, recipient_list=[user.email])
        return super().form_valid(form)

def valid_user_from_email(request, token):
    user = get_object_or_404(CustomUser, token=token)
    if user:
        user.is_active = True
        user.save()

    return PermissionDenied


