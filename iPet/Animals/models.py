from django.db import models

class Mascota(models.Model):
	mascota = models.ForeingKey()

class Precio (models.Model):
	precio = models.ForeignKey()

class Tamano (models.Model):
	tamano = models.ForeignKey()

class Mantenimiento (models.Model):
	mantenimiento = models.ForeignKey()

class Convivencia (models.Model):
	convivencia = models.ForeignKey()


class Ruido (models.Model):
	ruido = models.ForeignKey()


class Carisma (models.Model):
	carisma = models.ForeignKey()

