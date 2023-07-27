from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    units_sold = models.BigIntegerField()
    units_in_stock = models.BigIntegerField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug': self.slug
        })
