# Generated by Django 2.2.6 on 2020-10-12 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_transaction_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-payment_gateway_update_date']},
        ),
    ]
