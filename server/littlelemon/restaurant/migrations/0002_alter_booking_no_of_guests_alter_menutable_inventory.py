# Generated by Django 4.2.2 on 2023-06-21 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='menutable',
            name='inventory',
            field=models.IntegerField(),
        ),
    ]
