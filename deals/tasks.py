from celery import shared_task
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from accounts.models import Transaction
from deals.models import Deal

User = get_user_model()


@shared_task
def create_transaction_task(user_id, deal_id, total_price):
    user = User.objects.get(id=user_id)
    wallet = user.wallet
    deal = Deal.objects.get(id=deal_id)

    if deal.approved:
        wallet.balance += total_price
        wallet.save()

        transaction = Transaction.objects.create(
            deal=deal,
            value=total_price,
            wallet=wallet,
        )
