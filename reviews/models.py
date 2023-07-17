from django.db import models
class Rate(models.Choices):
    NOTE_0=0
    NOTE_1=1
    NOTE_2=2
    NOTE_3=3
    NOTE_4=4
    NOTE_5=5
    NOTE_6=6
    NOTE_7=7
    NOTE_8=8
    NOTE_9=9
    NOTE_10=10
class Status(models.TextChoices):
    I_WHANA_PLAY= "I whana play"
    PLAYNG="Playng"
    FINISHED= "Finished"
class Review(models.Model):
    review=models.TextField(max_length=6000, blank=True)
    published_at=models.DateField(auto_now=True)
    game_status = models.CharField(
        max_length=200,
        choices=Status.choices
    )
    rate=models.IntegerField(
        choices=Rate.choices,
        default=Rate.NOTE_0
    )
    game=models.ForeignKey(
        'games.Game', on_delete=models.CASCADE,related_name='reviews'
    )
    user=models.ForeignKey(
        'users.User',on_delete=models.CASCADE,related_name='reviews'
    )
    class Meta:
        unique_together = ('user', 'game')