from django.db import models
from django.contrib.auth.models import User
from Readinglist.models import Category, Topic, Author




class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True,)
    topics = models.ManyToManyField(Topic, blank=True,)
    views = models.PositiveIntegerField(default=0)  # Default to 0 views


    def __str__(self):
        return self.title

