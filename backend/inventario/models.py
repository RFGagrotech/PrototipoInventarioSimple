from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    codigo = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    precio = models.DecimalField(max_digits=8,decimal_places=2)
    disponible = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.cantidad}"

    