from django.db import models

# Create your models here.

class Project(models.Model):
    project = models.CharField(max_length=100)
    upload = models.ImageField(upload_to='uploads/')
    description = models.TextField(max_length=250)


