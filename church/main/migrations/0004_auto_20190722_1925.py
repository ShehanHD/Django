# Generated by Django 2.2.3 on 2019-07-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190722_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='db_event',
            field=models.CharField(max_length=50, verbose_name='Event'),
        ),
    ]
