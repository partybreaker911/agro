# Generated by Django 4.1.7 on 2023-03-04 10:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_remove_referralcode_referred_by_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="referralcode",
            old_name="referred_by",
            new_name="referred_users",
        ),
    ]
