# Generated by Django 2.2.6 on 2020-11-04 13:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_auto_20201104_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('language', models.CharField(choices=[('EN', 'ENGLISH'), ('BM', 'BAHASA MELAYU')], default='EN', max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]