# Generated by Django 4.2.3 on 2023-08-30 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_itemcategory_name_lowercase_alter_itemcategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcategory',
            name='name_lowercase',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
    ]
