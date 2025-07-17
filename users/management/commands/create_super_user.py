from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Добавление Супер пользователя"

    def handle(self, *args, **kwargs):
        user = User.objects.create(email = 'admin@admin.ru')
        user.set_password("1234")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()