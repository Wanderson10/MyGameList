# Generated by Django 4.2.2 on 2023-07-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_image",
            field=models.CharField(blank=True),
        ),
    ]
