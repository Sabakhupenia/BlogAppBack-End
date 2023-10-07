from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=50)
    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    def __str__(self):
        return self.name

