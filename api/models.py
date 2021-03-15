from django.db import models
# Create your models here.


class User(models.Model):
    userid = models.IntegerField(primary_key=True)  # primary keys are required by SQLAlchemy
    email = models.CharField(max_length=100, unique=True)
    fname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=1000)