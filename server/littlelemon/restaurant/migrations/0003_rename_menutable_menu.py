# Generated by Django 4.2.2 on 2023-06-21 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_no_of_guests_alter_menutable_inventory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuTable',
            new_name='Menu',
        ),
    ]
