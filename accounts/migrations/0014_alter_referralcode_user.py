# Generated by Django 4.1.7 on 2023-03-06 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0013_referralcode_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referralcode",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User refferal",
            ),
        ),
    ]
