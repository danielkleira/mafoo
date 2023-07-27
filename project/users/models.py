from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)
    
