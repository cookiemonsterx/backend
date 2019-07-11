from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    
    
    def __str__(self):
        return self.title



class Artist(models.Model):
    name = models.CharField(max_length=100, default= 'unknown')
    album = models.ForeignKey(
        Album, related_name='artist', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='song',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
