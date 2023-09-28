from rest_framework import viewsets
from products import models
from products.api import serializers
from rest_framework import permissions

class ProdutoViewSet(viewsets.ModelViewSet):
   queryset = models.Produto.objects.all()
   serializer_class = serializers.ProdutoSerializer
   permission_classes = [permissions.IsAuthenticated]

class CategoriaViewSet(viewsets.ModelViewSet):
   queryset = models.Categoria.objects.all()
   serializer_class = serializers.CategoriaSerializer
   permission_classes = [permissions.IsAuthenticated]
