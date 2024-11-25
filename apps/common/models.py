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




































