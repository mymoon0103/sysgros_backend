from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=225)
    email = models.CharField(max_length=225, unique=True)
    password = models.CharField(max_length=225)
    telephone = models.CharField(max_length=23, unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



# Create your models here.
