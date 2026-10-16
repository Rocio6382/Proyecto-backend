from rest_framework import serializers
from .models import Categoria, Proveedor, Producto, MovimientoInventario, AuditoriaEstado

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    proveedor_nombre = serializers.ReadOnlyField(source='proveedor.nombre_empresa')

    class Meta:
        model = Producto
        fields = '__all__'


class MovimientoInventarioSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.ReadOnlyField(source='producto.nombre')

    class Meta:
        model = MovimientoInventario
        fields = '__all__'


class AuditoriaEstadoSerializer(serializers.ModelSerializer):
    producto_sku = serializers.ReadOnlyField(source='producto.sku')

    class Meta:
        model = AuditoriaEstado
        fields = '__all__'