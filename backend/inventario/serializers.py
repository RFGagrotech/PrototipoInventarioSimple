from rest_framework import serializers
from .models import Producto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["codigo", "nombre", "categoria", "cantidad", "precio","disponible","fecha_registro",]
        read_only_fields = ["fecha_registro",]
