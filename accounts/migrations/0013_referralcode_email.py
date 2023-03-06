# Generated by Django 4.1.7 on 2023-03-06 23:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0012_profile_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="referralcode",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Invited Email"
            ),
        ),
    ]
