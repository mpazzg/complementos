from django.db import models
from django.contrib.auth.models import User


class cliente(models.Model):
	nombre		= models.CharField(max_length=200)
	apellidos	= models.CharField(max_length=200)
	telefono	= models.IntegerField()
	correo		= models.TextField(max_length=100)
	direccion	= models.TextField(max_length=100)

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
		return nombreCompleto
	
class producto(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
		return ruta

	def foto(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	foto.allow_tags = True

	nombre		= models.CharField(max_length=100)
	descripcion	= models.TextField(max_length=300)
	status		= models.BooleanField(default=True)
	precio		= models.DecimalField(max_digits=6,decimal_places=2) 
	stock		= models.IntegerField()
	imagen		= models.ImageField(upload_to=url)
	
	def __unicode__(self):
		return self.nombre

class compra(models.Model):
	cliente		= models.ForeignKey(cliente)
	producto 	= models.ForeignKey(producto)
	cantidad	= models.IntegerField()
	fecha		= models.DateField()
	
