# Generated by Django 4.1.7 on 2023-03-07 21:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0014_alter_referralcode_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ReferralCode",
        ),
    ]
