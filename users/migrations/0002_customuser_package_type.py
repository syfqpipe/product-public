# Generated by Django 2.2.6 on 2020-10-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='package_type',
            field=models.CharField(choices=[('01', 'Package 01'), ('02', 'Package 02'), ('03', 'Package 03'), ('04', 'Package 04'), ('NA', 'Not Available')], default='NA', max_length=2),
        ),
    ]
