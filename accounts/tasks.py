from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string


User = get_user_model()


def send_referral_email(self):
    pass
