# Generated by Django 4.1.2 on 2022-11-13 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emp', '0016_remove_emps_id_account'),
        ('product', '0004_rename_product_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_Order', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('id_emp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='emp.emps')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('id_Order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
                ('id_Product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.products')),
            ],
        ),
    ]
