# Generated by Django 4.1.7 on 2023-03-06 00:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0010_alter_referralcode_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Location ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Location")),
            ],
            options={
                "verbose_name": "Location",
                "verbose_name_plural": "Locations",
            },
        ),
    ]
