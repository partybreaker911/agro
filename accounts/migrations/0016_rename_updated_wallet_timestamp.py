# Generated by Django 4.1.7 on 2023-03-08 14:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0015_delete_referralcode"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wallet",
            old_name="updated",
            new_name="timestamp",
        ),
    ]
