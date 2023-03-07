from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from uuid import uuid4

User = get_user_model()


class Ticket(models.Model):
    id = models.UUIDField(
        _("Message ID"), primary_key=True, default=uuid4, unique=True, editable=False
    )
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    subject = models.CharField(_("Subject"), max_length=50)
    text = models.TextField(_("Message"))
    image = models.ImageField(_("Image"), upload_to="media/", blank=True, null=True)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = _("Message")
        verbose_name = _("Messages")

    def __str__(self) -> str:
        return f"{self.user} {self.subject}"
