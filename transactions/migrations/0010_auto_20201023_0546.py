# Generated by Django 2.2.6 on 2020-10-23 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_transaction_receipt_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='reference_no',
            new_name='reference',
        ),
        migrations.AddField(
            model_name='transaction',
            name='reference_id',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
