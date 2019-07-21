# Generated by Django 2.2.3 on 2019-07-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190712_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='type',
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'In progress'), ('Completed', 'Completed')], default=('Feature', 'Feature'), max_length=100),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], default=('Bug', 'Bug'), max_length=100),
        ),
    ]