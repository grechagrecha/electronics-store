from django.contrib import admin

from .models import Item, OrderedItem, Cart, ItemCategory


admin.site.register(Item)
admin.site.register(OrderedItem)
admin.site.register(Cart)
admin.site.register(ItemCategory)
