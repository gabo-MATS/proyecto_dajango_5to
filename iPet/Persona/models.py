from django.db import models
#Models Personas
class Persona(models.Model):
	edad = models.Charfield(max_length=100)
	alergia = models.Charfield(max_length=100)
	responsabilidad = models.Charfield(max_length=100)
	dinero = models.ForeignKey(Income)
# Create your models here.

class Income(models.Model):
	