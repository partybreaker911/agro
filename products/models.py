from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from accounts.models import Location
import uuid


class Category(MPTTModel):
    id = models.UUIDField(
        _("Category ID"),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    name = models.CharField(_("Name"), max_length=50)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categoryes")

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    id = models.UUIDField(
        _("Product ID"),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    category = models.ForeignKey(
        Category, verbose_name=_("Category"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Product"), max_length=50)
    available_points = models.PositiveIntegerField(default=10)
    sold_count = models.PositiveIntegerField(_("Sold Count"), default=0)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self) -> str:
        return self.name

    @property
    def get_price(self, location):
        try:
            return self.prices.get(location=location).price
        except ProductPrice.DoesNotExist:
            return None


class ProductPrice(models.Model):
    id = models.UUIDField(
        _("Product Price ID"),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    product = models.ForeignKey(
        Product, verbose_name=_("Product"), on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Location, verbose_name=_("Location"), on_delete=models.CASCADE
    )
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = [("product", "location")]
        verbose_name = _("Product Price")
        verbose_name_plural = _("Product Prices")

    def __str__(self) -> str:
        return self.product.name
