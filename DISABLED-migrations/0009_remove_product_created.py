# Generated by Django 4.2.1 on 2023-05-25 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
    ]
