# Generated by Django 4.1.7 on 2023-03-09 22:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0023_transaction"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="description",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Description"
            ),
        ),
    ]