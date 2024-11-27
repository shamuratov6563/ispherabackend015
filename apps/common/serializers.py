from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
    

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        exclude  = ("product",)
        

        
        
    
class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductPrice
        exclude = ("product","memory",)   
        
        
        
        
class ProductMemorySerializer(serializers.ModelSerializer):
    productprice_set = ProductPriceSerializer(many= True)
    class Meta:
        model = models.ProductMemory
        exclude = ("product",)    
        
        
    
    
class ProductDetailSerializer(serializers.ModelSerializer):
    productimage_set = ProductImageSerializer(many = True) 
    productmemory_set = ProductMemorySerializer(many = True)
    productprice_set = ProductPriceSerializer(many = True)
    
    
    class Meta:
        model = models.Product
        fields = '__all__'
        
        
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"    



        

    
