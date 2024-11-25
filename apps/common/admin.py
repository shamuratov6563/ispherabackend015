from django.contrib import admin
from apps.common.models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')
    list_filter = ('title',)
    search_fields = ('title', 'description')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_name', 'service')
    list_filter = ('service', 'category')
    search_fields = ('title', 'full_name')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'date')
    list_filter = ('category',)
    search_fields = ('name',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount', 'background_image')
    list_filter = ('discount',)
    search_fields = ('title',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'client_type', 'workplace')
    list_filter = ('client_type',)
    search_fields = ('full_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('promo_code', 'is_active', 'discount', 'min_price')
    list_filter = ('is_active',)
    search_fields = ('promo_code',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'total_price')
    list_filter = ('connection_type', 'payment_type', 'delivery')
    search_fields = ('full_name', 'email')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_avalible', 'delivery', 'service_duration', 'made_in')
    list_filter = ('is_avalible', 'made_in')
    search_fields = ('name',)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    list_filter = ('product',)
    search_fields = ('product__name',)


class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')
    list_filter = ('product',)
    search_fields = ('name',)


class ProductInfoTypeAdmin(admin.ModelAdmin):
    list_display = ('key', 'product_info')
    list_filter = ('product_info',)
    search_fields = ('key',)


class ProductMemoryAdmin(admin.ModelAdmin):
    list_display = ('memory', 'product')
    list_filter = ('product',)
    search_fields = ('memory',)


class ProductColourAdmin(admin.ModelAdmin):
    list_display = ('colour', 'product')
    list_filter = ('product',)
    search_fields = ('colour',)


class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'memory', 'price')
    list_filter = ('product', 'memory')
    search_fields = ('product__name',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_price', 'quantity')
    list_filter = ('order', 'product_price')
    search_fields = ('order__full_name',)


class Post2Admin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

admin.site.register(Post2, Post2Admin)


admin.site.register(Banner, BannerAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PromoCode, PromoCodeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
admin.site.register(ProductInfoType, ProductInfoTypeAdmin)
admin.site.register(ProductMemory, ProductMemoryAdmin)
admin.site.register(ProductColour, ProductColourAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
