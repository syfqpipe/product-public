# Generated by Django 2.2.6 on 2020-10-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201004_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsearchcriteria',
            name='total_page',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productsearchcriteria',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
