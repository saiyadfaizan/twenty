from django.contrib import admin
from .models import *
# Register your models here.


class AdminModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email']
    search_fields = ['name', 'email']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email']
    search_fields = ['name', 'email']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'description', 'digital']
    search_fields = ['name']
    list_filter =['category', 'digital']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'emailAddress', 'date_ordered', 'complete', 'transaction_id', 'status']
    search_fields = ['id', 'customer__name', 'emailAddress']
    list_filter =['complete', 'status', 'date_ordered']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'order', 'quantity', 'date_added']
    search_fields = ['date_added']
    list_filter =['date_added']

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added']
    search_fields = ['customer__name', 'order__emailAddress']
    list_filter =['city', 'state']


admin.site.register(Admin, AdminModel)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)