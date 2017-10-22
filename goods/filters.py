import django_filters
from django_filters.widgets import RangeWidget

from .models import GoodsBase


class GoodsFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt')
    edition_date = django_filters.DateFilter(name='edition_date', lookup_expr='gt')


    class Meta:
        model = GoodsBase
        fields = ['edition_date']
