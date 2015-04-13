from django.shortcuts import render
from django.http import HttpResponse
from complementos.apps.ventas.models import producto

from django.core import serializers


def wsProductos_view(request):
	data = serializers.serialize("json",producto.objects.filter(status=True))
	return HttpResponse(data,mimetype='application/json')
