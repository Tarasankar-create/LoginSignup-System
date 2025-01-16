from django.db import models

# Create your models here.
class user_master(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    roll_name= models.CharField(max_length=30)
    def __str__(self):
        return self.user_name
    