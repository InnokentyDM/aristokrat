from django.db.models import Q
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class CategoryGoodsList(ListView):
    model = GoodsBase

    context_object_name = 'goods'
    template_name = 'goods.html'
    paginate_by = 30

    def get_queryset(self):
        qs = GoodsBase.objects.filter(category__in=self.kwargs['id'] ,public=True).order_by('-edition_date')
        return qs


class GoodsDetail(DetailView):
    model = GoodsBase

    context_object_name = 'good'
    template_name = 'detail_goods.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(GoodsDetail, self).get_context_data(**kwargs)
        context['related'] = GoodsBase.objects.all().order_by('-id')[:3]
        return context


class Search(ListView):
    model = GoodsBase

    context_object_name = 'goods'
    template_name = 'goods.html'
    paginate_by = 30

    def get_queryset(self):
        search = self.kwargs['search']
        qs = GoodsBase.objects.filter(Q(name__contains=search) | Q(description__contains=search), public=True).order_by('-edition_date')
        return qs
