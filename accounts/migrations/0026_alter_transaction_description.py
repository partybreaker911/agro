# Generated by Django 4.1.7 on 2023-03-09 23:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0025_alter_transaction_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
    ]
