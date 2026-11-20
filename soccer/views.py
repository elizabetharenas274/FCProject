from django.shortcuts import render
from soccer.models import Equipo, Jugador

# Create your views here.

def home(request):
    return render(request, 'home.html')

def listadoJugadores(request):
    jugadores = Jugador.objects.all() # select * from Jugador
    return render(request, 'jugadores/listado_jugadores.html', {'jugadores': jugadores})

def listadoEquipos(request): #con clave foránea OMR de Django
    equipos = Equipo.objects.select_related('creador_id') #join entre equipo y jugador
    return render(request, 'equipos/listado_equipos.html', {'equipos': equipos})