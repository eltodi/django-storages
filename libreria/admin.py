#encoding:utf-8
from django.contrib import admin
from libreria.models import *

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
	list_display = ["titulo","archivo",]