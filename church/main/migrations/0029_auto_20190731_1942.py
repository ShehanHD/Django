# Generated by Django 2.2.3 on 2019-07-31 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20190731_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 19, 42, 32, 82206), verbose_name='date'),
        ),
    ]
