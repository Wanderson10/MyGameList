from django.db import models

class Gender(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    created_at= models.DateField(auto_now_add=True)
