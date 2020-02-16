from django.db import models

# Create your models here.

class Session(models.Model):
	
	movie = models.TextField(unique=True)
	joy = models.FloatField()
	sorrow = models.FloatField()
	anger = models.FloatField()
	surprise = models.FloatField()
	like_factor = models.FloatField()
	
	def __str__(self):
		return self.movie

class MusicSession(models.Model):
	
	artist = models.TextField(unique=True)
	joy = models.FloatField()
	sorrow = models.FloatField()
	anger = models.FloatField()
	surprise = models.FloatField()
	like_factor = models.FloatField()
	
	def __str__(self):
		return self.artist