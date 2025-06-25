from blackd import handle
from django.core.management import BaseCommand, call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help="Добавление текстовых данных из фикстуры"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'cat.json')
        self.stdout.write(self.style.SUCCESS('Успешно'))