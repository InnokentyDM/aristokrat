from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class CategoriesList(ListView):
    model = Categories

    context_object_name = 'categories'
    template_name = 'base.html'
    paginate_by = 30

    def get_queryset(self):
        qs = Categories.objects.all()
        return qs


