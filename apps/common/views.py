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
    
    
class ProductsCategoryAPIView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class CatalogAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.OrderCreateSerializer
    
    
    
    
    
# views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PromoCode
from .serializers import PromoCodeSerializer

@api_view(['POST'])
def apply_promo_code(request):
    promo_code = request.data.get('promo_code')
    total_price = request.data.get('total_price')

    if not promo_code or not total_price:
        return Response({"error": "Promo code and total price are required."}, status=400)

    try:
        promo = PromoCode.objects.get(promo_code=promo_code, is_active=True)
    except PromoCode.DoesNotExist:
        return Response({"error": "Invalid or inactive promo code."}, status=400)

    # Check if the total price meets the minimum price requirement
    if total_price < promo.min_price:
        return Response({"error": f"Minimum price requirement is {promo.min_price}."}, status=400)

    # Calculate the discount amount
    discount_amount = (promo.discount / 100) * total_price if promo.discount else 0
    discounted_price = total_price - discount_amount

    return Response({
        "discounted_price": discounted_price,
        "discount_amount": discount_amount,
        "original_price": total_price,
        "promo_code": promo_code,
    })


    

