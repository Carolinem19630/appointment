# Generated by Django 3.0.8 on 2020-08-28 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_attendees'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendees',
            new_name='Attendee',
        ),
    ]