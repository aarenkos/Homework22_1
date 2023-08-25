from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100, verbose_name='категория')
    price_for_purchase = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateField(verbose_name='дата создания')
    last_change_date = models.DateField(verbose_name='дата последнего изменения', auto_now_add=True)

    def __str__(self):
        return f'{self.name}, стоимость {self.price_for_purchase},категория {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
