# Generated by Django 2.2.3 on 2019-07-22 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190722_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 22, 19, 30, 16, 640426), verbose_name='date'),
        ),
    ]
