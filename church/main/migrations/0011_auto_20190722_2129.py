# Generated by Django 2.2.3 on 2019-07-22 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190722_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(default=1, height_field=200, upload_to='pics/about', width_field=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 22, 21, 29, 17, 415764), verbose_name='date'),
        ),
    ]
