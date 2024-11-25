from django.db import models


class Main(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='main/')
    url = models.URLField()

    def __str__(self):
        return self.title

class Post(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class Service(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    date = models.DateTimeField()


class SpecialOffers(models.Model):
    title = models.CharField(max_length=255)
    discount = models.IntegerField()
    background_image = models.ImageField(upload_to='special_offers/')

    def __str__(self):
        return self.title

class Clients(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clients/')
    client_type = models.URLField()
    workplace = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class Posts(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title
    






class Category(models.Model):
    name = models.CharField(max_length=255)  # agar Category modeli mavjud bosa

    def __str__(self):
        return self.name




# SHOP qismi
# 
# class Sponsor(models.Model):
#     class choices(models.TextChoices):
#         NEW = "new", "yangi"
#         MODERNATION = "modernation", "modernation"
#         APPROVED = "approved", "approved"
#         CANCELLED = "cancelled", "cancelled"
#     class choices2(models.TextChoices):
#         KARTA_ORQALI = "karta_orqali", "karta_orqali"
#         NAQD = "naqd", "naqd"
#     class choices3(models.TextChoices):
#         PERSONAL = "personal", "personal"
#         LEGAL = "legal", "legal"
#     full_name = models.CharField(max_length=32)
#     phone_number = models.IntegerField()
#     donation_amout = models.IntegerField()
#     org_name = models.CharField(max_length=255)
#     type = models.CharField(max_length=255, choices=choices3)
#     status = models.CharField(max_length=255, choices=choices, default=choices.NEW)
#     created_at = models.DateTimeField(auto_now_add=True)
#     payment_type = models.CharField(max_length=200, choices=choices2, null=True)




class PromoCode(models.Model):
    promo_code = models.CharField(max_length=20)
    is_active = models.BooleanField()
    discount = models.DecimalField()
    






class Order(models.Model):
    class choices(models.TextChoices):
        PHONE_CALL = 'PhoneCall','Call'
        EMAIL = 'email','gmail'
        
    class choices2(models.TextChoices):
        CASH = 'money', 'cash'
        CREDIT_CARD = 'credit','card'
        
        
    class choices3(models.Choices):
        BY_YOURSELF = 'own','yourself'
        DELIVERY_MOSCOW = 'InMoscow','Moscow'
        DELIVERY_RUSSIA = 'russia', 'Russia'
                
        
         
    full_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField()
    connection_way = models.CharField(max_length=200,choices=choices)
    comment = models.TextField()
    payment_type = models.CharField(max_length=200,choices=choices2)
    delivery = models.CharField(max_length=200,choices=choices3)
    total_price = models.DecimalField()
    promocode = models.ForeignKey(PromoCode,on_delete=models.PROTECT)
    
    
    

    
class OrderItem(models.Model):
    product_price = models.ForeignKey('PRODUCT_PRICE',on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
        
    

class Product(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    is_avalible = models.BooleanField()
    delivery = models.CharField(max_length=255)
    pickup = models.CharField(max_length=125)
    pickup = models.CharField(max_length=65)
    service_duration = models.CharField(max_length=65)
    made_in = models.CharField(max_length=65)
    guarantee = models.CharField(max_length=65)



class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_image/')
    product = models.ForeignKey(Product)


class ProductInfo(models.Model):
    name = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)



class ProductInfoType(models.Model):
    key = models.CharField(max_length=250)
    key = models.CharField(max_length=250)
    product_info = models.ForeignKey(ProductInfo, on_delete=models.PROTECT)


class ProductMemory(models.Model):
    memory = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.PROTECT) 


class ProductColour(models.Model):
    colour = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.PROTECT) 



class ProductPrice(models.Model):    
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    memory= models.ForeignKey(ProductMemory, on_delete=models.PROTECT)
    price = models.IntegerField()
































