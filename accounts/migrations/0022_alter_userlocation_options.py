# Generated by Django 4.1.7 on 2023-03-09 20:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0021_remove_profile_address"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userlocation",
            options={
                "verbose_name": "User Location",
                "verbose_name_plural": "Users Locations",
            },
        ),
    ]