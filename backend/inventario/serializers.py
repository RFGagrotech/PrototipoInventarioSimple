from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["codigo", "nombre", "categoria", "cantidad", "precio","disponible","fecha_registro",]
        read_only_fields = ["fecha_registro",]
