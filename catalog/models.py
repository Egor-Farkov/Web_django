from django.db import models

from users.models import CustomUser


# Create your models here.

class Category(models.Model):
    """Модель категории"""

    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    """Модель продуктов"""

    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    purchase_price = models.PositiveIntegerField(verbose_name='цена',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='владелец', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
        permissions = [('can_unpublish_product', 'может отменять публикацию продукта'),
                      ('can_delete_product', 'может удалять публикацию продукта')]

