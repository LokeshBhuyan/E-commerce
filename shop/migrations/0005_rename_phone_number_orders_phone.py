# Generated by Django 5.0 on 2024-05-04 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='phone_number',
            new_name='phone',
        ),
    ]