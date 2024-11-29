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


class ProductSerializer(serializers.ModelSerializer):
    productimage_set = ProductImageSerializer(many = True) 
    productmemory_set = ProductMemorySerializer(many = True)
    productprice_set = ProductPriceSerializer(many = True)
    class Meta:
        model = models.Product
        fields = '__all__'
            

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = ('product_price', 'quantity')
    

class OrderCreateSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True, write_only=True)
    

    class Meta:
        model = models.Order
        exclude = ('total_price', )
        extra_kwargs = {
            'orderitem_set': {
                "write_only": True
            }
        }

    def create(self, validated_data):
        orderitem_set = validated_data.pop('orderitem_set')
        instance = models.Order.objects.create(**validated_data)
        total_price = 0
        for order_item in orderitem_set:
            models.OrderItem.objects.create(**order_item, order=instance)
            total_price += order_item['quantity'] * order_item['product_price'].price

        instance.total_price = total_price
        instance.save()
        return instance
    
    # TODO validation check promocode is valid or not 
    
    
    
class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PromoCode
        fields = ['promo_code', 'is_active', 'discount', 'min_price']