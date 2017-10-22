from django.contrib import admin
from .models import *


class ImagesInline(admin.TabularInline):
    model = Images


class GoodsBaseAdmin(admin.ModelAdmin):
    readonly_fields = ['edition_date']
    inlines = [ImagesInline]
    save_as = True

    class Meta:
        model = GoodsBase

class PicturesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'public', 'genre', 'author', 'creation_date', 'size']
    filter_horizontal = ('category',)
    readonly_fields = ['edition_date']
    inlines = [ImagesInline]
    save_as = True

    class Meta:
        model = Pictures

admin.site.register(Pictures, PicturesAdmin)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'public']
    filter_horizontal = ('category',)
    inlines = [ImagesInline]
    save_as = True

    class Meta:
        model = Goods

admin.site.register(Goods, GoodsAdmin)


class AntiquesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    list_display = ['id', 'name', 'description', 'price', 'public']
    filter_horizontal = ('category',)
    save_as = True

    class Meta:
        model = Antiques

admin.site.register(Antiques, AntiquesAdmin)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ["id", "image"]

    class Meta:
        model = Images

admin.site.register(Images, ImagesAdmin)



