import os
from django.db import models
from django.utils.safestring import mark_safe

from categories.models import Categories
from references.models import Genres




class GoodsBase(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name='Название')
    description = models.TextField(null=True, blank=True, default=None, verbose_name='Описание')
    price = models.IntegerField(null=True, blank=True, default=None, verbose_name='Цена')
    edition_date = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата добавления')
    public = models.BooleanField(verbose_name='Публикация')
    category = models.ForeignKey(Categories, blank=True, null=True, default=None, verbose_name='Категории')
    author = models.CharField(max_length=100, null=True, blank=True, default=None, verbose_name='Автор')
    creation_date = models.DateField(default=None, blank=True, null=True, verbose_name='Период создания')
    genre = models.ForeignKey(Genres, blank=True, null=True, default=None, verbose_name='Жанр')

class Images(models.Model):
    image = models.ImageField()
    good = models.ForeignKey(GoodsBase, blank=True, null=True, default=None)

    def url(self):
        return str(self.image.url)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

# class Goods(GoodsBase):
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Товар'
#         verbose_name_plural = 'Другие товары'


# class Pictures(GoodsBase):
#     size = models.CharField(max_length=12, blank=True, null=True, default=None, verbose_name='Размер')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Картина'
#         verbose_name_plural = 'Картины'


class Antiques(GoodsBase):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Антиквариат'
        verbose_name_plural = 'Антиквариат'
