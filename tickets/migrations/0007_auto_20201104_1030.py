# Generated by Django 2.2.6 on 2020-11-04 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20201104_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketsubject',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketTopic'),
        ),
    ]
