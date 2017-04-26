from django.db import models

# Create your models here.
class Animals (models.Model):
	price = models.IntegerField(default=0)
	size = models.IntegerField(default=0)
	maintenance = models.IntegerField(default=0)
	life = models.IntegerField(default=0)
	