# Generated by Django 2.2.6 on 2020-10-03 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20201003_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='address',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='email_address',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='organisation',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='phone_number',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
