from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from uuid import uuid4
from catalogs.models import Location, Product

User = get_user_model()


class Warehouse(models.Model):
    id = models.UUIDField(
        _("Warehouse ID"), primary_key=True, default=uuid4, unique=True, editable=False
    )
    user = models.OneToOneField(
        User, verbose_name=_("User"), on_delete=models.SET_NULL, null=True, blank=True
    )
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    class Meta:
        verbose_name = _("Warehouse")
        verbose_name_plural = _("Warehouses")

    def __str__(self) -> str:
        return f"{self.user}"


class WarehouseDetail(models.Model):
    id = models.UUIDField(
        _("WarehouseDetail ID"),
        primary_key=True,
        default=uuid4,
        unique=True,
        editable=False,
    )
    warehouse = models.OneToOneField(
        Warehouse, verbose_name=_("Warehouse"), on_delete=models.CASCADE
    )
    capacity = models.IntegerField(_("Capacity"))
    location = models.ForeignKey(
        Location, verbose_name=_("Location"), on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    class Meta:
        verbose_name = _("Warehouse Detail")
        verbose_name_plural = _("Warehouses Details")

    def __str__(self) -> str:
        return f"{self.warehouse} {self.capacity}"


class WarehouseItem(models.Model):
    id = models.UUIDField(
        _("Items ID"), primary_key=True, default=uuid4, unique=True, editable=False
    )
    warehouse = models.ForeignKey(
        Warehouse, verbose_name=_("Warehouse"), on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, verbose_name=_("Product"), on_delete=models.CASCADE
    )
    quantity = models.IntegerField(_("Quantity"))
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    class Meta:
        verbose_name = _("Warehouse Item")
        verbose_name_plural = "Warehouses Items"

    def __str__(self) -> str:
        return f"{self.warehouse} {self.product}"
