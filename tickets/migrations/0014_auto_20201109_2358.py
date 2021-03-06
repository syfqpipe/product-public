# Generated by Django 2.2.6 on 2020-11-09 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_auto_20201109_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquirymedia',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_attachments', to='tickets.Ticket'),
        ),
        migrations.AlterField(
            model_name='enquiryticketreply',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_replies', to='tickets.Ticket'),
        ),
    ]
