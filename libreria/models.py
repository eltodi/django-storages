#encoding:utf-8

from django.db import models

class Documento(models.Model):
	titulo = models.CharField(max_length=200)
	archivo = models.FileField(upload_to="documentos")
	portada = models.ImageField(upload_to="portadas", null=True)

	def __unicode__(self):
		return u"%s" %(self.titulo)
