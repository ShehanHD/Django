# Generated by Django 2.2.3 on 2019-07-31 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20190731_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 19, 2, 8, 141728), verbose_name='date'),
        ),
    ]