from django.contrib import admin
from django.urls import path, include #cagar a modulo principal (include)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicaciones.urls')), #carga la ruta del modulo aplicaciones en el principal  
    path('accounts/', include('django.contrib.auth.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)