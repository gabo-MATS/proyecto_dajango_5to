from django.db import models
#Models Personas
class Persona(models.Model):
	edad = models.CharField(max_length=100)
	alergia = models.CharField(max_length=100)
	responsabilidad = models.CharField(max_length=100)
	#dinero = models.ForeignKey(Income)
# Create your models here.

#class Income(models.Model):
#	presupuesto=models.IntergerField()
	