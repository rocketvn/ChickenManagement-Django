# Generated by Django 4.1.2 on 2022-10-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emps',
            name='date',
            field=models.DateField(default='2001-01-01'),
        ),
        migrations.AlterField(
            model_name='emps',
            name='gender',
            field=models.CharField(choices=[('other', 'Other'), ('male', 'Male'), ('female', 'Female')], default='male', max_length=6),
        ),
    ]
