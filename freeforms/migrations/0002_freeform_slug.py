# Generated by Django 2.2.6 on 2020-10-14 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeforms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='freeform',
            name='slug',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
