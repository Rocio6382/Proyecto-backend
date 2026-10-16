from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Proveedor, Producto, MovimientoInventario, AuditoriaEstado
from .serializers import (
    CategoriaSerializer, ProveedorSerializer, ProductoSerializer,
    MovimientoInventarioSerializer, AuditoriaEstadoSerializer
)

# Vistas para HTML tradicional (Puntos 6 y 7 del README)
def bienvenida(request):
    return render(request, 'bienvenida.html')

def pagina_no_encontrada(request, exception=None):
    return render(request, 'error404.html', status=404)

# Vistas para API REST (Django REST Framework - Punto 15)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class MovimientoInventarioViewSet(viewsets.ModelViewSet):
    queryset = MovimientoInventario.objects.all().order_by('-fecha_movimiento')
    serializer_class = MovimientoInventarioSerializer


class AuditoriaEstadoViewSet(viewsets.ModelViewSet):
    queryset = AuditoriaEstado.objects.all().order_by('-fecha_cambio')
    serializer_class = AuditoriaEstadoSerializer