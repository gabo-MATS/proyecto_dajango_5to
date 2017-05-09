from django.db import models

# Create your models here.
class Animals (models.Model):
	price = models.IntegerField(default=0)
	size = models.ForeignKey(Size)
	maintenance = models.IntegerField(default=0)
	life = models.ForeignKey(Life)
	time = models.ForeignKey(Time)
	noise = models.ForeignKey(Noise)
	rare = models.ForeignKey(Rarity)
	
class Size(models.Model):
	size = models.CharField(max_length=20)

class Life(models.Model):
	life = models.IntegerField(default=0)

class Time(models.Model):
	time = models.IntegerField(default=0)

class Noise(models.Model):
	noise = models.IntegerField(default=0)

class Rarity(models.Model):
	rare = models.CharField(max_length=20)




