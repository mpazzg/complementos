from django.contrib import admin
from complementos.apps.ventas.models import cliente,producto


class productoAdmin(admin.ModelAdmin):
	list_display = ('nombre','thumbnail','precio','stock')
	list_filter = ('nombre','precio')
	search_fields = ('nombre','precio')
	fields = ('nombre','descripcion',('precio','stock'),'imagen','status')



admin.site.register(cliente)
admin.site.register(producto,productoAdmin)
