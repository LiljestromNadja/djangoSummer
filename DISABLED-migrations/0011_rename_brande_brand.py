# Generated by Django 4.2.1 on 2023-05-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_rename_brand_brande'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brande',
            new_name='Brand',
        ),
    ]
