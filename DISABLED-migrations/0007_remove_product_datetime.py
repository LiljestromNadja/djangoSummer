# Generated by Django 4.2.1 on 2023-05-25 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='datetime',
        ),
    ]