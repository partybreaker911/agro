from django.db import models
from django.utils.translation import gettext_lazy as _

from uuid import uuid4
from mptt.models import MPTTModel, TreeForeignKey


class ProductCategory(MPTTModel):
    id = models.UUIDField(
        _("Category ID"), primary_key=True, default=uuid4, unique=True, editable=False
    )
    name = models.CharField(_("Category"), max_length=50)
    parent = TreeForeignKey(
        "self",
        verbose_name=_("SubCategory"),
        on_delete=models.CASCADE,
        related_name="parent_category",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Products Categorys")

    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    id = models.UUIDField(
        _("Product ID"), primary_key=True, default=uuid4, unique=True, editable=False
    )
    category = models.ForeignKey(
        ProductCategory, verbose_name=_("Category"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Product"), max_length=50)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self) -> str:
        return f"{self.category.name} {self.name}"


class State(models.Model):
    id = models.UUIDField(
        _("State ID"), primary_key=True, default=uuid4, unique=True, editable=False
    )
    name = models.CharField(_("State"), max_length=50)

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self) -> str:
        return self.name


class Region(models.Model):
    id = models.UUIDField(
        _("Region ID"), primary_key=True, default=uuid4, unique=True, editable=False
    )
    name = models.CharField(_("Region"), max_length=50)
    state = models.ForeignKey(
        State, verbose_name=_("State"), on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    id = models.UUIDField(
        _("Location ID"), primary_key=True, default=uuid4, unique=True, editable=False
    )
    name = models.CharField(_("Location"), max_length=50)
    region = models.ForeignKey(
        Region,
        verbose_name=_("Region"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self) -> str:
        return self.name
