# Generated by Django 2.2.6 on 2020-10-29 06:36

import core.helpers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
        ('services', '0031_egovernmentrequest_approver'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentrequestitem',
            name='document_type',
            field=models.CharField(choices=[('FR', 'Form'), ('PF', 'Profile')], default='FR', max_length=2),
        ),
        migrations.AddField(
            model_name='documentrequestitem',
            name='entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.Entity'),
        ),
        migrations.AddField(
            model_name='documentrequestitem',
            name='generated_profile',
            field=models.FileField(null=True, upload_to=core.helpers.PathAndRename('document-request-item-profile')),
        ),
        migrations.AlterField(
            model_name='documentrequestitem',
            name='image_form_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='documentrequestitem',
            name='image_version_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
