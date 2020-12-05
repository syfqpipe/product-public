# Generated by Django 2.2.6 on 2020-10-29 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0035_auto_20201029_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentrequestitem',
            name='approved',
        ),
        migrations.AddField(
            model_name='documentrequestitem',
            name='approver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_request_approver', to=settings.AUTH_USER_MODEL),
        ),
    ]
