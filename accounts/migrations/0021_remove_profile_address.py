# Generated by Django 4.1.7 on 2023-03-08 15:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0020_remove_userlocation_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="address",
        ),
    ]
