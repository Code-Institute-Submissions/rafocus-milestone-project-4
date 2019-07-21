# Generated by Django 2.2.3 on 2019-07-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_ticket_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='funding',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='ticket',
            name='funding_target',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
