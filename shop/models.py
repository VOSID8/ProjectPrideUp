from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    
    def __str__(self):
        return str(self.user.username)
    

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    address = models.TextField()

    def __str__(self):
        return str(self.user.username)

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.FloatField()
    desc = models.TextField()
    quantity = models.PositiveIntegerField()
    discount = models.IntegerField()
    image1 = models.ImageField(upload_to='shop/static/shop/images/products', null=True)
    image2 = models.ImageField(upload_to='shop/static/shop/images/products', null=True)
    image3 = models.ImageField(upload_to='shop/static/shop/images/products', null=True)
    image4 = models.ImageField(upload_to='shop/static/shop/images/products', null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(default = 0)

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    name = models.CharField(max_length = 80)
    email = models.CharField(max_length = 100)
    query = models.CharField(max_length = 300)

    def __str__(self) -> str:
        return str(self.id)