from django.db import models
class precio(models.Model):
class Mascota(models.Model):

	precio = models.Charfield(max_length=100)
	tamano = models.Charfield(max_length=100)
	mantenimiento = models.Charfield(max_length=100)
	convivencia = models.Charfield(max_length=100)
	vida = models.Charfield(max_length=100)
	ruido = models.Charfield(max_length=100)
	carisma = models.Charfield(max_length=100)

class Persona(models.Model):
	edad = models.Charfield(max_length=100)
	alergia = models.Charfield(max_length=100)
	responsabilidad = models.Charfield(max_length=100)
	dinero = models.Charfield(max_length=100)