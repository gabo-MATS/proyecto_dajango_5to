from django.db import models

# Create your models here.
class Animals (models.Model):
	price = models.IntegerField(default=0)
	size = models.CharField(max_length=20)
	maintenance = models.IntegerField(default=0)
	life = models.IntegerField(default=0)
	time = models.IntegerField(default=0)
	noise = models.IntegerField(default=0)
	rare = models.CharField(max_length=20)
