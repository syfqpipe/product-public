# Generated by Django 2.2.6 on 2020-10-29 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0034_documentrequest_reference_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentrequest',
            old_name='offical_letter_request',
            new_name='official_letter_request',
        ),
    ]
