# Generated by Django 4.1.7 on 2023-03-04 00:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_wallet_balance"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="birth_date",
            field=models.DateField(blank=True, null=True, verbose_name="Birth Date"),
        ),
    ]
