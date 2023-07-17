from django.db import models


class Game(models.Model):
    name_game=models.CharField(unique=True,max_length=300)
    description = models.TextField(max_length=1000)
    game_logo=models.CharField(max_length=300)
    made_by=models.CharField(max_length=200)
    genders=models.ManyToManyField('genders.Gender', related_name='games')
