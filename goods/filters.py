import django_filters
from django_filters.widgets import RangeWidget, LookupTypeWidget, BaseCSVWidget, CSVWidget

from .models import GoodsBase


class GoodsFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    # creation_date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'filter-input'}), name='creation_date', lookup_expr='gt')
    # edition_date = django_filters.DateRangeFilter(name='edition_date')
    creation_date__gt = django_filters.DateFilter(name='creation_date', lookup_expr='gt')
    creation_date__lt = django_filters.DateFilter(name='creation_date', lookup_expr='lt')
    price_gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    price_lt = django_filters.NumberFilter(name='price', lookup_expr='lt')
    author = django_filters.CharFilter(name='author')
    # edition_date = django_filters.DateFilter(name='edition_date', lookup_expr='gt')


    class Meta:
        model = GoodsBase
        fields = ['category', 'author', 'genre']
