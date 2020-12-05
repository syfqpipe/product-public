# Generated by Django 2.2.6 on 2020-09-30 23:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='NA', max_length=100)),
                ('local_or_foreign', models.CharField(choices=[('LC', 'Local'), ('FR', 'Foreign')], default='LC', max_length=2)),
                ('type_of_entity', models.CharField(choices=[('AD', 'Audit'), ('BS', 'Business'), ('CP', 'Company'), ('CS', 'Company Secratery')], default='CP', max_length=2)),
                ('check_digit', models.CharField(default='NA', max_length=2)),
                ('registration_number', models.CharField(default='NA', max_length=20)),
                ('registration_number_new', models.CharField(default='NA', max_length=20)),
                ('company_number', models.CharField(default='NA', max_length=20)),
                ('company_number_new', models.CharField(default='NA', max_length=20)),
                ('audit_firm_number', models.CharField(default='NA', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]