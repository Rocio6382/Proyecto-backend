from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventario_pyme_app.urls')),
]

# Manejador de error 404 personalizado
handler404 = 'inventario_pyme_app.views.pagina_no_encontrada'