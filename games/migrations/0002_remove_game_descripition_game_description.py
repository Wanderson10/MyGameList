# Generated by Django 4.2.2 on 2023-07-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="game",
            name="descripition",
        ),
        migrations.AddField(
            model_name="game",
            name="description",
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
