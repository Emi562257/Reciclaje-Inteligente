from djongo import models

class Usuario(models.Model):
    _id = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
class CentroVerde(models.Model):
    _id = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.TextField()
    capacidad = models.IntegerField()
    horario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre
class Registro(models.Model):
    _id = models.CharField(max_length=20, primary_key=True)
    usuario = models.CharField(max_length=20)  # podría ser ForeignKey, pero Djongo usa CharField para referencias simples
    centro_verde = models.CharField(max_length=20)
    material = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registro {self._id} - Usuario {self.usuario}"
class Estadistica(models.Model):
    _id = models.CharField(max_length=20, primary_key=True)
    material = models.CharField(max_length=20)
    total_cantidad = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Estadistica {self._id} - Material {self.material}"
class ProductoCanjeable(models.Model):
    _id = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos_requeridos = models.IntegerField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
