from django.db import models

# Create your models here.
# after creating  every model use command 'makemigrations', which will create a database schema 

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
