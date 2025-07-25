from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Добавление пользователей и прав"

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'fixture_users.json')
        self.stdout.write(self.style.SUCCESS('Успешно'))