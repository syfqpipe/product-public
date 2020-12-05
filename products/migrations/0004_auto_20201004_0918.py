# Generated by Django 2.2.6 on 2020-10-04 09:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_delete_customsearchquota'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSearchCriteria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('incorp_date_from', models.CharField(max_length=100)),
                ('incorp_date_to', models.CharField(max_length=100)),
                ('company_status', models.CharField(default='NA', max_length=100)),
                ('company_type', models.CharField(default='NA', max_length=100)),
                ('company_origin', models.CharField(default='NA', max_length=100)),
                ('company_location', models.CharField(default='NA', max_length=100)),
                ('division', models.CharField(default='NA', max_length=100)),
                ('business_code', models.CharField(default='NA', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('MS', 'Malay'), ('NA', 'Not Available')], default='EN', max_length=2),
        ),
    ]
