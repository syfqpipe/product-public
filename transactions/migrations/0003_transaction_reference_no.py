# Generated by Django 2.2.6 on 2020-10-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20201003_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='reference_no',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
