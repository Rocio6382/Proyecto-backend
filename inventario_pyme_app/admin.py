from django.contrib import admin
from .models import Categoria, Proveedor, Producto, MovimientoInventario, AuditoriaEstado

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'created_at')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_empresa', 'rut', 'email', 'activo')
    search_fields = ('nombre_empresa', 'rut')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'precio', 'stock', 'estado', 'categoria', 'proveedor')
    list_filter = ('estado', 'categoria', 'proveedor')
    search_fields = ('sku', 'nombre')

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo_movimiento', 'cantidad', 'usuario_registro', 'fecha_movimiento')

@admin.register(AuditoriaEstado)
class AuditoriaEstadoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'estado_anterior', 'estado_nuevo', 'fecha_cambio')
# Register your models here.
