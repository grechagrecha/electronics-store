# Generated by Django 4.2.3 on 2023-08-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(auto_created=models.CharField(max_length=255), blank=True, unique=True),
        ),
    ]