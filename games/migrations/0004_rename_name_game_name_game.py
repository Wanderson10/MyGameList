# Generated by Django 4.2.2 on 2023-07-07 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0003_alter_game_users_avaliations"),
    ]

    operations = [
        migrations.RenameField(
            model_name="game",
            old_name="name",
            new_name="name_game",
        ),
    ]
