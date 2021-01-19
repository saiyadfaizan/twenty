from rest_framework import serializers
from store.models import *


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ('user', 'name', 'email')
        
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('user', 'name', 'email')
        
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        #fields = ('name', 'category', 'price', 'description', 'digital', 'image')
        
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        #fields = ('customer', 'emailAddress', 'date_ordered', 'complete', 'transaction_id', 'status')

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ('product', 'order', 'quantity', 'date_added')

class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = '__all__'
        