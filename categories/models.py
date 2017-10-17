import os
from django.db import models



class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название',blank=True, null=True, default=None)
    menu_title = models.CharField(max_length=50, verbose_name='Текст ссылки', blank=True, null=True, default=None)

    def __str__(self):
        return "Категория %s" % self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


