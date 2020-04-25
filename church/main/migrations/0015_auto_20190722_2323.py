# Generated by Django 2.2.3 on 2019-07-22 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190722_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(blank=True, height_field='200', upload_to='pics/about', width_field='200'),
        ),
        migrations.AlterField(
            model_name='services',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 22, 23, 23, 55, 83552), verbose_name='date'),
        ),
    ]
