from django import forms

from support.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (
            "subject",
            "text",
            "image",
        )
