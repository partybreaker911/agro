from django import forms

from support.models import Ticket, Reply


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (
            "subject",
            "text",
            "image",
        )


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = (
            "text",
            "image",
        )
