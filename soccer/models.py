from django.db import models

# Create your models here.

class Jugador(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=150)
    telefono = models.CharField(max_length=20)
    posicion = models.CharField(max_length=30)
    nivel = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.id_jugador


class Cancha(models.Model):
    id_cancha = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.id_cancha


class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ciudad = models.CharField(max_length=100)
    creador_id = models.ForeignKey(Jugador, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_equipo


class Partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    cupos = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)
    equipo_local_id = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_local')
    equipo_visitante_id = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_visitante')
    organizador_id = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    cancha_id = models.ForeignKey(Cancha, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_partido


class Torneo(models.Model):
    id_torneo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ciudad = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20)
    organizador_id = models.ForeignKey(Jugador, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_torneo   

class Convocatoria(models.Model):
    id_convocatoria = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    cupos = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    organizador_id = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    cancha_id = models.ForeignKey(Cancha, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_convocatoria

    