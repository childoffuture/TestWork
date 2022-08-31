from django.db import models


# Create your models here.
class Link(models.Model):
    name = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
