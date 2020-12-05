# Generated by Django 2.2.6 on 2020-10-24 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_package_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='agency_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='egov_request',
        ),
        migrations.AddField(
            model_name='customuser',
            name='egov_expired_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
