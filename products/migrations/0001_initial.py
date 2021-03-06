# Generated by Django 2.2.6 on 2020-09-30 23:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='NA', max_length=100)),
                ('description', models.TextField(default='NA')),
                ('slug', models.CharField(default='NA', max_length=100)),
                ('fee', models.IntegerField(default=0)),
                ('output_type', models.CharField(choices=[('DO', 'Document'), ('IM', 'Image'), ('LI', 'List')], default='CP', max_length=2)),
                ('ctc', models.BooleanField(default=True)),
                ('language', models.CharField(choices=[('EN', 'English'), ('MS', 'Malay')], default='EN', max_length=2)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
