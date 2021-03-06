# Generated by Django 2.2.6 on 2020-11-15 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0012_refunddropdown'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='card_holder',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='card_no_mask',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
