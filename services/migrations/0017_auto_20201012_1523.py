# Generated by Django 2.2.6 on 2020-10-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_egovernmentrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='product_type',
            field=models.CharField(choices=[('ST', 'Statistics'), ('LS', 'Listing'), ('NA', 'Not Available')], default='NA', max_length=2),
        ),
    ]
