from django.db import models

# Create your models here.
class Login(models.Model) : 
    id = models.CharField(max_length = 20, primary_key=True)
    password = models.CharField(max_length = 20)