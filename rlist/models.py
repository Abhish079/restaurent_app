from django.db import models


# Create your models here
class Entry(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Owner = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Type = models.CharField(max_length=6)
    Date = models.DateField( auto_now_add=True )


class lentry(models.Model):
    Username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password_1= models.CharField(max_length=50)
    password_2= models.CharField(max_length=50)
