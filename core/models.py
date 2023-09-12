from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.conf import settings


class ItemAttribute(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}: {self.value}'


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    units_sold = models.BigIntegerField()
    units_in_stock = models.BigIntegerField()
    slug = models.SlugField(unique=True, blank=True, editable=False)
    main_image = models.ImageField(default='', upload_to='img/', blank=True)
    featured = models.BooleanField(default=False)

    attributes = models.ManyToManyField(ItemAttribute, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={
            'slug': self.slug
        })

    def create_slug(self):
        return f'{slugify(self.name)}'

    def save(self, *args, **kwargs):
        self.slug = self.create_slug()
        super(Item, self).save(*args, **kwargs)


class OrderedItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedItem)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(default=None)

    def __str__(self):
        return f'{self.user}\'s cart'


class ItemCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Item categories'

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, default='')
    name_lowercase = models.CharField(max_length=200, default='', blank=True)
    image = models.ImageField(default='', upload_to='img/', blank=True)
    items = models.ManyToManyField(Item)
    number_of_items = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return f'{self.name} ({self.number_of_items} items)'

    def save(self, *args, **kwargs):
        self.name_lowercase = str(self.name).lower()
        super().save(*args, **kwargs)
