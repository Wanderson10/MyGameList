# Generated by Django 4.2.2 on 2023-07-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("genders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gender",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]