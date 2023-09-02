from django import template
from core.models import Cart

register = template.Library()


@register.filter
def card_item_count(user):
    if user.is_authenticated:
        qs = Cart.objects.filter(user=user, ordered=False)
        if qs.exists():
            count = 0

            for item in qs[0].items.all():
                count += item.quantity

            return count
    return 0
