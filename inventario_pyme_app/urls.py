from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crear enrutador de Django REST Framework
router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'proveedores', views.ProveedorViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'movimientos', views.MovimientoInventarioViewSet)
router.register(r'auditoria-estados', views.AuditoriaEstadoViewSet)

urlpatterns = [
    # 1. La raíz '' cargará la vista de bienvenida (bienvenida.html)
    path('', views.bienvenida, name='bienvenida'),
    
    # 2. Las rutas API quedarán agrupadas bajo '/api/'
    path('api/', include(router.urls)),
]