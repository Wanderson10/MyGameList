# Generated by Django 4.2.2 on 2023-07-14 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_remove_userimage_user_userimage_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userimage",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_image",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
