# Generated by Django 4.1.7 on 2023-03-09 20:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("catalogs", "0005_alter_productcategory_parent"),
        ("deals", "0002_deal_product"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="deal",
            options={
                "ordering": ["-timestamp"],
                "verbose_name": "Deal",
                "verbose_name_plural": "Deals",
            },
        ),
        migrations.CreateModel(
            name="ProductPrice",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, verbose_name="Price"
                    ),
                ),
                ("works_until", models.DateTimeField(verbose_name="Works Until")),
                (
                    "timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="Timestamp"),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.location",
                        verbose_name="Location",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogs.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Price",
                "verbose_name_plural": "Products Prices",
                "ordering": ["-timestamp"],
            },
        ),
    ]
