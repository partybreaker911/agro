from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

import uuid
from products.models import Product

User = get_user_model()


class Deal(models.Model):
    BUY = "B"
    SELL = "S"
    DEAL_TYPE_CHOICES = [
        (BUY, _("Buy")),
        (SELL, _("Sell")),
    ]
    id = models.UUIDField(
        _("Deal ID"), primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Product"),
    )
    quantity = models.PositiveIntegerField(_("Quantity"), default=0)
    type = models.CharField(_("Type"), max_length=1, choices=DEAL_TYPE_CHOICES)
    approved = models.BooleanField(_("Approved"), default=False)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    class Meta:
        verbose_name = _("Deal")
        verbose_name_plural = _("Deals")

    def __str__(self) -> str:
        return f"{self.user} {self.product} {self.quantity} {self.approved}"
