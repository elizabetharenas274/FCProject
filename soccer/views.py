from django.shortcuts import render, get_object_or_404, redirect
from soccer.models import Cancha, Equipo, Jugador
from soccer.forms import EquipoForm, JugadorForm, CanchaForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def listadoJugadores(request):
    jugadores = Jugador.objects.all() # select * from Jugador
    return render(request, 'jugadores/listado_jugadores.html', {'jugadores': jugadores})

def registrarJugador(request):
    if request.method == 'POST':
        formulario = JugadorForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listado_jugadores')
    else:
        formulario = JugadorForm()
    return render(request, 'jugadores/formulario_jugadores.html', {'formulario': formulario})

def listadoEquipos(request): #con clave foránea OMR de Django
    equipos = Equipo.objects.select_related('creador_id') #join entre equipo y jugador
    return render(request, 'equipos/listado_equipos.html', {'equipos': equipos})

def detalleEquipos(request, equipo_id):
    equipo = get_object_or_404(Equipo, id_equipo=equipo_id)
    return render(request, 'equipos/detalle_equipos.html', {'equipo': equipo})

def registrarEquipo(request):
    if request.method == 'POST':
        formulario = EquipoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listado_equipos')
    else:
        formulario = EquipoForm()
    return render(request, 'equipos/formulario_equipos.html', {'formulario': formulario})

def listadoCanchas(request):
    canchas = Cancha.objects.all()
    return render(request, 'canchas/listado_canchas.html', {'canchas': canchas})

def registrarCancha(request):
    if request.method == 'POST':
        formulario = CanchaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listado_canchas')
    else:
        formulario = CanchaForm()
    return render(request, 'canchas/formulario_canchas.html', {'formulario': formulario})