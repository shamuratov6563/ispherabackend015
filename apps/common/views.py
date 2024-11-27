from django.shortcuts import render
from rest_framework import generics
from . import models, serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.views import Response

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ProductSerializer
    
    
class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ProductDetailSerializer
    queryset = models.Product.objects.all()
    
    
class BannerAPIView(APIView):
    serializer_class = serializers.BannerSerializer
    queryset = models.Banner.objects.all()
    
class CategoryAPIView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Banner.objects.all()
    
    
class ProductImageAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.all()
    
    
