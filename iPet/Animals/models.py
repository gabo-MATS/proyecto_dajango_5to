from django.db import models
#Models Animals
class precio(models.Model):
	precio = models.Charfield(max_length=100)

class tamano(models.Model):
	tamano = models.Charfield(max_length=100)

class mantenimiento(models.Model):
	mantenimiento = models.Charfield(max_length=100)

class vida(models.Model):
	vida = models.Charfield(max_length=100)

class convivencia(models.Model):
	convivencia = models.Charfield(max_length=100)

class ruido(models.Model):
	ruido = models.Charfield(max_length=100)	

class Mascota(models.Model):
	carisma = models.Charfield(max_length=100)
