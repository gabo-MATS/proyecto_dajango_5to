from django.db import models

# Create your models here.
class Animals (models.Model):
	precio = models.IntegerField(default=0)