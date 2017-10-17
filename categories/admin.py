from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'menu_title']

    class Meta:
        model = Categories

admin.site.register(Categories, CategoriesAdmin)

