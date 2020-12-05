# Generated by Django 2.2.6 on 2020-10-03 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20201003_0506'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='service',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='service_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceRequest'),
        ),
    ]