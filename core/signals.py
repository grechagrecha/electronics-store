from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ItemCategory


@receiver(post_save, sender=ItemCategory, dispatch_uid='update_category')
def update_category(sender, instance, **kwargs):
    """
        !!! WIP !!!

        - Sets category image to image of one of the items
        - Updates item count
    """
    items_m2m_qs = instance.items.all()
    img = items_m2m_qs.order_by('name').first().main_image

    sender.objects.filter(id=instance.id).update(image=img, number_of_items=instance.items.count())

    print('Item category updated!')
