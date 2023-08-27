from django import template
from core.models import Cart

register = template.Library()


@register.filter
def card_item_count(user):
    if user.is_authenticated:
        qs = Cart.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
