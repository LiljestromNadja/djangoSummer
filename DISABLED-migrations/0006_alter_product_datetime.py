# Generated by Django 4.2.1 on 2023-05-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime',
            field=models.DateTimeField(default=True),
        ),
    ]
