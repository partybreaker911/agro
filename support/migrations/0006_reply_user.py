# Generated by Django 4.1.7 on 2023-03-07 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("support", "0005_alter_ticket_options_alter_reply_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="reply",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]