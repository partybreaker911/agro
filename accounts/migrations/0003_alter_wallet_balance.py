# Generated by Django 4.1.7 on 2023-03-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_wallet_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="balance",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Balence"
            ),
        ),
    ]
