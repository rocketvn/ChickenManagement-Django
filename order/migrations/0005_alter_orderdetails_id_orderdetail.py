# Generated by Django 4.1.2 on 2022-11-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_orderdetails_delete_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='id_orderdetail',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]