from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания (записи в БД)')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Дата последнего изменения (записи в БД)')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} {self.price}'
