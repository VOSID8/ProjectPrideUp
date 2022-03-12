from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['userName', 'phone', 'userEmail', 'address']
    def userName(self, obj):
        return obj.user.username
    def userEmail(self, obj):
        return obj.user.email

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['userName', 'phone', 'userEmail', 'address']
    def userName(self, obj):
        return obj.user.username
    def userEmail(self, obj):
        return obj.user.email

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'seller_name', 'quantity', 'price']
    def seller_name(self, obj):
        return obj.seller.user.username

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'productsCount']
    def productsCount(self, obj):
        return len(obj.products)

@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['productName', 'customerName', 'quantity']
    def productName(self, obj):
        return obj.product.name
    def customerName(self, obj):
        return obj.customer.user.username

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['productName', 'customerName', 'quantity', 'status', 'date']
    def productName(self, obj):
        return obj.product.name
    def customerName(self, obj):
        return obj.customer.user.username

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')