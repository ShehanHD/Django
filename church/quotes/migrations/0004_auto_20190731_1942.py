# Generated by Django 2.2.3 on 2019-07-31 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20190731_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='to',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
