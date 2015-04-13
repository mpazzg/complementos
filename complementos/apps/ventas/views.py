from django.shortcuts import render_to_response
from django.template import RequestContext
from complementos.apps.ventas.forms import addProductForm
from complementos.apps.ventas.models import producto
from django.http import HttpResponseRedirect


def add_product_view(request):
	info = "Inicializando"
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProductForm(request.POST,request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				imagen = form.cleaned_data['imagen']
				precio = form.cleaned_data['precio']
				stock = form.cleaned_data['stock']
				p = producto()
				if imagen:
					p.imagen = imagen
				p.nombre = nombre
				p.descripcion = descripcion
				p.precio = precio
				p.stock = stock
				
				p.status = True
				p.save()
				info = "Se guardo satisfactoriamente"
			else:
				info = "Informacion con datos incorrectos"
		form = addProductForm()
		ctx = {'form':form,'informacion':info}
		return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))

	else:
		return HttpResponseRedirect('/')

