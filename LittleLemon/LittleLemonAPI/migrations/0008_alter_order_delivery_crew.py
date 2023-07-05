# Generated by Django 4.2.2 on 2023-06-17 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LittleLemonAPI', '0007_alter_order_delivery_crew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_crew',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='delivery_crew', to=settings.AUTH_USER_MODEL),
        ),
    ]