# Generated by Django 2.2.6 on 2020-10-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20201005_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_status',
            field=models.CharField(choices=[('CM', 'Completed'), ('AB', 'Abandoned'), ('CR', 'Created'), ('NA', 'Not Available')], default='CR', max_length=2),
        ),
    ]
