from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=300, default="")
    time = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return title
2