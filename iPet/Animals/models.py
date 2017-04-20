from django.db import models
#Models Animals
class Precio(models.Model):
	precio = models.IntegerField(default=0)

class Tamano(models.Model):
	tamano = models.IntegerField(default=0)

class Mantenimiento(models.Model):
	mantenimiento = models.CharField(max_length=100)

class Vida(models.Model):
	vida = models.CharField(max_length=100)

class Convivencia(models.Model):
	convivencia = models.CharField(max_length=100)

class Ruido(models.Model):
	ruido = models.CharField(max_length=100)	

class Carisma(models.Model):
	carisma = models.CharField(max_length=100)
