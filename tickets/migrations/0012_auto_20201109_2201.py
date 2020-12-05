# Generated by Django 2.2.6 on 2020-11-09 22:01

import core.helpers
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_auto_20201109_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('attached_document', models.FileField(null=True, upload_to=core.helpers.PathAndRename('enquiry-attached-document'))),
            ],
        ),
        migrations.RenameField(
            model_name='ticketsubject',
            old_name='name',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='tickettopic',
            old_name='name',
            new_name='name_en',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='attached_document',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='tel_number',
        ),
        migrations.AddField(
            model_name='ticketsubject',
            name='name_bm',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='tickettopic',
            name='name_bm',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
