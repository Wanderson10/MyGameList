# Generated by Django 4.2.2 on 2023-07-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0012_alter_review_rate_alter_review_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="game_status",
            field=models.CharField(
                choices=[
                    ("I whana play", "I Whana Play"),
                    ("Playng", "Playng"),
                    ("Finished", "Finished"),
                ],
                default=1,
                max_length=200,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="review",
            name="rate",
            field=models.IntegerField(
                choices=[
                    (0, "Note 0"),
                    (1, "Note 1"),
                    (2, "Note 2"),
                    (3, "Note 3"),
                    (4, "Note 4"),
                    (5, "Note 5"),
                    (6, "Note 6"),
                    (7, "Note 7"),
                    (8, "Note 8"),
                    (9, "Note 9"),
                    (10, "Note 10"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="review",
            field=models.TextField(blank=True, max_length=6000),
        ),
    ]
