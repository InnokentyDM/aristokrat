import os
from django.db import models


class Genres(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Стиль')

    class Meta:
        verbose_name_plural = 'Стили'
        verbose_name = 'Стиль'

    def __str__(self):
        return self.name


# class Authors(models.Model):
#     name = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='ФИО')
#
#     class Meta:
#         verbose_name_plural = 'Авторы'
#         verbose_name = 'Автор'
#
#     def __str__(self):
#         return self.name