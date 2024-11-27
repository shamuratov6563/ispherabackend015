from rest_framework import serializers
from . import models



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        exclude  = ("product",)
        

        
        
    
class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductPrice
        exclude = ("product","memory",)   
        
        
        
        
# class ProductMemorySerializer(serializers.ModelSerializer):
#     productprice_set = ProductPriceSerializer(many= True)
#     class Meta:
#         model = models.ProductMemory
#         exclude = ("product",)    
        
        
from rest_framework import serializers
from . import models

class ProductMemorySerializer(serializers.ModelSerializer):
    # Using SerializerMethodField to add the price
    price = serializers.SerializerMethodField()

    class Meta:
        model = models.ProductMemory
        
        fields = ['id', 'memory', 'price']  # Only include id, memory, and price

    def get_price(self, obj):
        """
        Custom method to retrieve the price for the ProductMemory instance.
        Here you can add custom logic to get the price.
        """
        # Assuming you want the first price associated with this ProductMemory.
        # You can customize this logic based on your use case.
        price = obj.productprice_set.first()  # Get the first ProductPrice related to this ProductMemory
        return price.price if price else None  # Return price or None if no price is available






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
    productimage_set = ProductImageSerializer(many = True) 
    class Meta:
        model = models.Category
        fields = "__all__"    


<<<<<<< HEAD







=======
class ProductSerializer(serializers.ModelSerializer):
    productimage_set = ProductImageSerializer(many = True) 
    productmemory_set = ProductMemorySerializer(many = True)
    productprice_set = ProductPriceSerializer(many = True)
    class Meta:
        model = models.Product
        fields = '__all__'
    
>>>>>>> 26a716554c9e34546c3537b45737091844eb7b31
        

    
