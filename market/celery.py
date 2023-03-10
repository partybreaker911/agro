import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market.settings")

app = Celery()
app.config_from_object("market.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
