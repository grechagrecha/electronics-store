import django_filters
from django_filters.widgets import RangeWidget

from .models import Item, ItemCategory


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Name'
    )
    price = django_filters.NumericRangeFilter(
        field_name='price',
        label='Price',
        widget=RangeWidget()
    )
    category = django_filters.ModelChoiceFilter(
        queryset=ItemCategory.objects.all(),
        field_name='itemcategory',
        label='Category'
    )

    class Meta:
        model = Item
        exclude = [
            'name',
            'description',
            'main_image',
            'units_sold',
            'units_in_stock',
            'slug',
            'attributes',
            'featured'
        ]
