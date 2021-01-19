import django_filters
from .models import *


class CategoryFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ['category']
       

class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = ['status']
       