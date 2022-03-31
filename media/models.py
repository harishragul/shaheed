from django.core.files.storage import default_storage
from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    main = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Animation(models.Model):
    video = models.FileField(upload_to='animations/')
    description = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    main = models.BooleanField(default=False)
    image = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Music(models.Model):
    audio = models.FileField(upload_to='music/')
    thumbnail = models.ImageField(upload_to='music/')
    description = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    main = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Simulation(models.Model):
    video = models.FileField(upload_to='simulation/')
    description = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    main = models.BooleanField(default=False)

    def __str__(self):
        return self.description