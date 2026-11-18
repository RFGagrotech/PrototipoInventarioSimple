from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "categoria", "cantidad", "precio", "disponible", "fecha_registro",)
    search_fields = ("nombre",)
    list_filter = ("nombre", "categoria", "disponible",)