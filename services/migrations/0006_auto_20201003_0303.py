# Generated by Django 2.2.6 on 2020-10-03 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20201003_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='city',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='country',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='postcode',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
