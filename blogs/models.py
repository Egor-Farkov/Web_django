from django.db import models

# Create your models here.
class Blog(models.Model):
    """Модель блога"""

    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images/')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    sign_publication = models.BooleanField(verbose_name='Признак публикации', default=True)
    count_view = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
