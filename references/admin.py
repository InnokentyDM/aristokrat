from django.contrib import admin
from .models import *


class GenresAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

    class Meta:
        model = Genres

admin.site.register(Genres, GenresAdmin)

# class AuthorsAdmin(admin.ModelAdmin):
#     list_display = ["id", "name"]
#
#     class Meta:
#         model = Authors
#
# admin.site.register(Authors, AuthorsAdmin)