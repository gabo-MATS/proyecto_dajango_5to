from django.db import models
class Person(models.Model):	
	age = models.IntegerField(default=0)
	alergies = models.CharField(max_length=200)
	responsable = models.IntegerField(default=0)
	income = models.IntegerField(default=0)