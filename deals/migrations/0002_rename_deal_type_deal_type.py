# Generated by Django 4.1.7 on 2023-03-07 13:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("deals", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="deal",
            old_name="deal_type",
            new_name="type",
        ),
    ]
