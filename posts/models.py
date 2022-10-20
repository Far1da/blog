from abc import update_abstractmethods
from socket import create_server
from turtle import title
from django.db import models
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text  = models.Field(max_length=500)
    created_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"Post{self.title}"