from django.contrib import admin

from .models import Item, OrderedItem, Cart, ItemCategory, ItemAttribute


admin.site.register(Item)
admin.site.register(OrderedItem)
admin.site.register(Cart)
admin.site.register(ItemCategory)
admin.site.register(ItemAttribute)
