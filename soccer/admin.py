from django.contrib import admin

# Register your models here.

from.models import Jugador, Cancha, Equipo, Partido, Torneo, Convocatoria

admin.site.register(Jugador)
admin.site.register(Cancha)
admin.site.register(Equipo)
admin.site.register(Partido)
admin.site.register(Torneo)
admin.site.register(Convocatoria)