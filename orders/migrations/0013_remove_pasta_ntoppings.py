# Generated by Django 3.0.6 on 2020-06-10 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200610_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasta',
            name='ntoppings',
        ),
    ]
