from django.db import models
#Models Animals
class Precio(models.Model):
	precio = models.Charfield(max_length=100)

class Tamano(models.Model):
	tamano = models.Charfield(max_length=100)

class Mantenimiento(models.Model):
	mantenimiento = models.Charfield(max_length=100)

class Vida(models.Model):
	vida = models.Charfield(max_length=100)

class Convivencia(models.Model):
	convivencia = models.Charfield(max_length=100)

class Ruido(models.Model):
	ruido = models.Charfield(max_length=100)	

class Carisma(models.Model):
	carisma = models.Charfield(max_length=100)
