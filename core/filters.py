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
            'class': 'form-select'
        })
    )

    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='',
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name'
        })
    )
    price = django_filters.RangeFilter(
        field_name='price',
        label='Price',
        lookup_expr='range',
        widget=RangeWidgetWith2Placeholders(
            attrs={
                'class': 'form-control mb-1'
            },
            from_attrs={
                'class': 'mb-5',
                'placeholder': 'Price from'
            },
            to_attrs={
                'placeholder': 'Price to'
            }

        )
    )

    class Meta:
        model = Item
        fields = {

        }
