from django.db import models


class Banner(models.Model):
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
    date = models.DurationField()


class Discount(models.Model):
    title = models.CharField(max_length=255)
    discount = models.IntegerField()
    background_image = models.ImageField(upload_to='special_offers/')

    def __str__(self):
        return self.title

class Client(models.Model):
    class ClientType(models.TextChoices):
        person = 'Person', 'person'
        company = 'Company', 'company'
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clients/')
    client_type = models.CharField(max_length=200, choices=ClientType.choices)
    workplace = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=255)  

    def __str__(self):
        return self.name


class PromoCode(models.Model):
    promo_code = models.CharField(max_length=20)
    is_active = models.BooleanField()
    discount = models.PositiveIntegerField()
    min_price = models.PositiveIntegerField()
    

class Order(models.Model):
    class ConnectionType(models.TextChoices):
        PHONE = 'PHONE','phone'
        MAIL = 'MAIL','mail'
        
    class PaymentType(models.TextChoices):
        CASH = 'CASH', 'cash'
        CREDIT = 'CREDIT','credit'
        
        
    class DeliveryType(models.TextChoices):
        OWN = 'Own','own'
        DELIVERY_MOSCOW = 'InMoscow', 'moscow'
        DELIVERY_RUSSIA = 'RUSSIA', 'russia'
         
    full_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField()
    connection_type = models.CharField(max_length=200,choices=ConnectionType.choices)
    comment = models.TextField()
    payment_type = models.CharField(max_length=200,choices=PaymentType.choices)
    delivery = models.CharField(max_length=200,choices=DeliveryType.choices)
    total_price = models.PositiveIntegerField()
    promocode = models.ForeignKey(PromoCode,on_delete=models.PROTECT)
    


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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


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


class OrderItem(models.Model):
    product_price = models.ForeignKey(ProductPrice,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
        
    


































