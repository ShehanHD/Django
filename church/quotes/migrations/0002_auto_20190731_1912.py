# Generated by Django 2.2.3 on 2019-07-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quotes',
            options={'verbose_name_plural': 'Quotes'},
        ),
        migrations.AddField(
            model_name='quotes',
            name='book',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotes',
            name='fro',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quotes',
            name='to',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quotes',
            name='verse',
            field=models.IntegerField(default=0),
        ),
    ]