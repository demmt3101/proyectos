# Generated by Django 4.2.4 on 2023-09-13 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_events_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='hora',
            field=models.TimeField(),
        ),
    ]