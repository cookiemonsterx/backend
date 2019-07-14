from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    
    
    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ManyToManyField(Album)

    def __str__(self):
        return self.title





class Artist(models.Model):
    name = models.CharField(max_length=100)
    album = models.ManyToManyField(Album)
    song = models.ManyToManyField(Song)
  
    
    def __str__(self):
        return self.name



