from django.db import models



from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(unique=True, blank=False )
    date_joined=models.DateField(auto_now_add=True)
    # user_image= models.ImageField(upload_to='media/', blank=True)

class UserImage(models.Model):
    user_image= models.ImageField(upload_to='media/')
    user=models.OneToOneField('users.User', related_name='user_image',on_delete=models.CASCADE)