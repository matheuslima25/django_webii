from rest_framework import serializers
from products import models

class ProdutoSerializer(serializers.ModelSerializer):
   class Meta:
     model = models.Produto
     fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
     model = models.Categoria
     fields = '__all__'
