# Generated by Django 4.1.2 on 2022-11-09 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_id_emp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='id_category',
        ),
    ]
