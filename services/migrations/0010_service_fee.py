# Generated by Django 2.2.6 on 2020-10-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20201003_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='fee',
            field=models.IntegerField(default=1000),
        ),
    ]
