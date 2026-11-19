from django.shortcuts import render
from soccer.models import Jugador

# Create your views here.

def listadoJugadores(request):
    jugadores = Jugador.objects.all() # select * from Jugador
    return render(request, 'jugadores/listado_jugadores.html', {'jugadores': jugadores})
