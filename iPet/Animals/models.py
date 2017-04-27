from django.db import models
<<<<<<< HEAD

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
=======
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

<<<<<<< HEAD
class ruido(models.Model):
	ruido = models.Charfield(max_length=100)	

class Mascota(models.Model):
	carisma = models.Charfield(max_length=100)
>>>>>>> origin/master
=======
class Ruido(models.Model):
	ruido = models.CharField(max_length=100)	
>>>>>>> origin/master

class Carisma(models.Model):
	carisma = models.CharField(max_length=100)
