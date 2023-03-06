from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

from accounts.models import ReferralCode

User = get_user_model()


@shared_task
def send_referral_email(referrer_email, referred_email):
    referrer = User.objects.get(email=referrer_email)
    rederred = User.objects.get(email=referred_email)
    # Get user code
    referral_code = ReferralCode.objects.get(user=referrer).code
    subject = "You've been invited to join our site!"
    from_email = settings.DEFAULT_EMAIL_FROM
    to_email = referred_email
    context = {
        "referrer": referrer,
        "referred": rederred,
        "referral_code": referral_code,
        "site_url": settings.SITE_URL,
    }
    html_context = render_to_string("account/email/referral_email.html", context)
    text_context = render_to_string("account/email/referral_email.txt", context)
    email = EmailMessage(subject, text_context, from_email, [to_email])
    email.attach_alternative(html_context, "text/html")
    email.send()
