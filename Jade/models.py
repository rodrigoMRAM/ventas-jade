from django.db import models
from datetime import datetime   

DIRECIONES = (
    ('Las palmas 2731', 'Las palmas 2731'),
    ('Las palmas 2779', 'Las palmas 2779'),
    ('Las palmas 2838','Las palmas 2838'),
    ('Las palmas 2850', 'Las palmas 2850'),
    ('Las palmas 2856', 'Las palmas 2856'),
    ('Las palmas 2876', 'Las palmas 2876'),
    ('Corrales 1123', 'Corrales 1123'),
    ('Ramirez 970','Ramirez 970'),
)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}- Precio:  {self.precio}"
    

class Ventas(models.Model):
    direccion = models.CharField(max_length=100, choices=DIRECIONES, default='Perro')
    piso = models.SmallIntegerField()
    departamento = models.CharField(max_length=1)
    descripcion = models.TextField(max_length=100)
    total = models.IntegerField()
    fecha = models.DateField(default=datetime.now)
    def save(self, *args, **kwargs):
        # Convertir el valor del campo nombre a mayúsculas antes de guardar
        self.departamento = self.departamento.upper()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.direccion}- Piso:{self.piso}- Departamento: {self.departamento}"