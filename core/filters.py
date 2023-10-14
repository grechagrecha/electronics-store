import django_filters
from django.forms.widgets import TextInput, Select

from .models import Item, ItemCategory
from core.widgets.widgets import RangeWidgetWith2Placeholders


class ItemFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=ItemCategory.objects.all(),
        field_name='itemcategory',
        lookup_expr='exact',
        label='Category',
        empty_label='All',
        widget=Select(attrs={
            'class': 'form-select mb-1'
        })
    )

    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='',
        widget=TextInput(attrs={
            'class': 'form-control mb-1',
            'placeholder': 'Name'
        })
    )
    price = django_filters.NumericRangeFilter(
        field_name='price',
        label='Price',
        lookup_expr='range',
        widget=RangeWidgetWith2Placeholders(
            from_attrs={
                'placeholder': 'Price from'
            },
            to_attrs={
                'placeholder': 'Price to'
            },
            attrs={
                'class': 'form-control mb-1'
            }
        )
    )


    class Meta:
        model = Item
        fields = {

        }
