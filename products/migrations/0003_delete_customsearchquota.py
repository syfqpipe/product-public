# Generated by Django 2.2.6 on 2020-10-04 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_customsearchquota'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomSearchQuota',
        ),
    ]