from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.conf import settings


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class ItemAttributeValue(BaseModel):
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.value


class ItemAttribute(BaseModel):
    name = models.CharField(max_length=200)
    values = models.ManyToManyField(ItemAttributeValue)

    def __str__(self):
        return self.name


class Item(BaseModel):
    class ItemCategoryChoices(models.TextChoices):
        LAPTOPS = 'LA'
        COMPUTER_MICE = 'CM'
        WATCHES = 'WA'
        CPUS = 'CP'
        GPUS = 'GP'
        MONITORS = 'MO'

    objects = models.Manager()

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=100)
    units_sold = models.BigIntegerField(default=0)
    units_in_stock = models.BigIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    main_image = models.ImageField(default='', upload_to='img/items/', blank=True)
    featured = models.BooleanField(default=False)

    attributes = models.ManyToManyField(ItemAttribute, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug': self.slug
        })

    def get_attributes_key_value_pairs(self):
        attributes = dict()

        for attribute in self.attributes.all():
            breakpoint()

    def get_add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={
            'slug': self.slug
        })

    def create_slug(self):
        return f'{slugify(self.name)}'

    def save(self, *args, **kwargs):
        self.slug = self.create_slug()
        super(Item, self).save(*args, **kwargs)


class OrderedItem(BaseModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'


class Cart(BaseModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedItem)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(default=None)

    def __str__(self):
        return f'{self.user}\'s cart'


class ItemCategory(BaseModel):
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
