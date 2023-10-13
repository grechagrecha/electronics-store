import django_filters
from django_filters.widgets import RangeWidget
from django.forms.widgets import TextInput, Select

from .models import Item, ItemCategory


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Name',
        widget=TextInput(attrs={
            'class': 'form-control mb-1'
        })
    )
    price = django_filters.NumericRangeFilter(
        field_name='price',
        label='Price range',
        lookup_expr='range',
        widget=RangeWidget(attrs={
            'class': 'form-control mb-1'
        })
    )
    category = django_filters.ModelChoiceFilter(
        queryset=ItemCategory.objects.all(),
        field_name='itemcategory',
        lookup_expr='exact',
        label='Category',
        widget=Select(attrs={
            'class': 'form-select mb-1'
        })
    )

    class Meta:
        model = Item
        fields = {

        }
