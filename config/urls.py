from django.contrib import admin
from django.urls import include, path
from soccer.views import listadoJugadores
from django.conf import settings
from django.conf.urls.static import static
import soccer.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jugadores/', listadoJugadores),
    #path('', include('soccer.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )