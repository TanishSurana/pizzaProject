# Generated by Django 3.0.6 on 2020-06-10 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_remove_pasta_ntoppings'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinnerplatter',
            name='sizeEnable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pasta',
            name='sizeEnable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='regularpizza',
            name='sizeEnable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='salad',
            name='sizeEnable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sicilianpizza',
            name='sizeEnable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subs',
            name='sizeEnable',
            field=models.BooleanField(default=True),
        ),
    ]