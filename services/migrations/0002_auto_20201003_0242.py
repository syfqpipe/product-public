# Generated by Django 2.2.6 on 2020-10-03 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('CB', 'CBID'), ('IN', 'Investigation'), ('NA', 'Not Available')], default='PD', max_length=2),
        ),
    ]
