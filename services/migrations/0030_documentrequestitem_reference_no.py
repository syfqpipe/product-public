# Generated by Django 2.2.6 on 2020-10-25 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0029_egovernmentrequest_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentrequestitem',
            name='reference_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
