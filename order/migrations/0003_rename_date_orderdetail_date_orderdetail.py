# Generated by Django 4.1.2 on 2022-11-13 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderdetail_date_alter_order_id_emp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='date',
            new_name='date_orderdetail',
        ),
    ]
