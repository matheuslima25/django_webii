from rest_framework import routers
from products.api import viewsets

product_router = routers.DefaultRouter()
product_router.register('produto', viewsets.ProdutoViewSet)
product_router.register('categoria', viewsets.CategoriaViewSet)
