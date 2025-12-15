from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product, Collection, OrderItems
from .serializers import ProductSerializer, CollectionSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    def get_serialize_context(self):
        return {'request': self.request} 

    def destroy(self, request, *args, **kwargs):
        if OrderItems.objects.filter(product_id=kwargs['pk']).exists():
            return Response({'error': 'Product cannot be deleted because it is in use'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer