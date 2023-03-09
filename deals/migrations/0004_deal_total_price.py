# Generated by Django 4.1.7 on 2023-03-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deals", "0003_alter_deal_options_productprice"),
    ]

    operations = [
        migrations.AddField(
            model_name="deal",
            name="total_price",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Total Price"
            ),
        ),
    ]
