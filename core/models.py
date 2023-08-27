from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.conf import settings


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    units_sold = models.BigIntegerField()
    units_in_stock = models.BigIntegerField()
    slug = models.SlugField(unique=True, blank=True, editable=False)
    main_image = models.ImageField(default='', upload_to='img/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={'slug': self.slug})

    def create_slug(self):
        return f'{slugify(self.name)}'

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)
        self.slug = self.create_slug()


class OrderedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return 'ordered item' + self.item.name


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedItem)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(default=None)

    def __str__(self):
        return f'user: {self.user} items: {self.items.all()} date: {self.ordered_date}'


class ItemCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(default='', upload_to='img/', blank=True)
    items = models.ManyToManyField(Item)
    number_of_items = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return f'{self.name} ({self.number_of_items} items)'
