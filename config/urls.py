from django.contrib import admin
from django.urls import include, path
#from soccer.views import listadoEquipos, listadoJugadores
from django.conf import settings
from django.conf.urls.static import static
from soccer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('jugadores/', views.listadoJugadores, name='listado_jugadores'),
    path('equipos/', views.listadoEquipos, name='listado_equipos'),

    #path('jugadores/', listadoJugadores),
    #path('equipos/', listadoEquipos),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )