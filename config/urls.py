from django.contrib import admin
from django.urls import include, path
#from soccer.views import listadoEquipos, listadoJugadores
from django.conf import settings
from django.conf.urls.static import static
from soccer import views
#from soccer.views import listadoEquipos, listadoJugadores, registrarEquipo, detalleEquipos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('jugadores/', views.listadoJugadores, name='listado_jugadores'),
    path('jugadores/registrar/', views.registrarJugador, name='registrarJugador'),
    path('equipos/', views.listadoEquipos, name='listado_equipos'),
    path('equipos/<int:equipo_id>/', views.detalleEquipos, name='detalle_equipos'),
    path('equipos/registrar/', views.registrarEquipo, name='registrarEquipo'),
    path('canchas/', views.listadoCanchas, name='listado_canchas'),
    path('canchas/registrar/', views.registrarCancha, name='registrarCancha'),

    #path('jugadores/', listadoJugadores),
    #path('equipos/', listadoEquipos),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )