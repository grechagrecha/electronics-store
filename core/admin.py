from django.contrib import admin

from .models import Item, OrderedItem, ShoppingCart, ItemCategory


admin.site.register(Item)
admin.site.register(OrderedItem)
admin.site.register(ShoppingCart)
admin.site.register(ItemCategory)
