# Generated by Django 3.0.6 on 2020-06-06 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200607_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='subs',
            name='extrasEnable',
            field=models.BooleanField(default=True),
        ),
    ]