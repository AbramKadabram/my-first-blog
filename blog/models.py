from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):

    title = models.CharField('Заголовок', max_length=100)
    opisanie = models.TextField('Краткое описание', max_length=300, default='')
    text = models.TextField('Текст', max_length=10000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(verbose_name='Изоброжение', default=True)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    '''Характеристика категорий товаров'''
    title = models.CharField('Название категории',max_length=15, blank=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    '''Характеристика товара'''
    category = models.ForeignKey(ProductCategory, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название товара', max_length=100, blank=False)
    description = models.TextField(verbose_name='Описание товара', blank=False)
    image = models.ImageField(verbose_name='Изоброжение товара', blank=False)
    price = models.CharField(verbose_name='Цена', max_length=30)

    def __str__(self):
        return self.title

class ImgLoader(models.Model):
    '''Загрузка изоброжения'''

    name = models.CharField(verbose_name='Название изоброжения', max_length=15)
    image = models.ImageField('Изоброжение', default='image')










