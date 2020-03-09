from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Catelogy, Product, Shipping, Order, Rating
from.serializers import UserSerializer, CatelogySerializer, ProductSerializer, ShippingSerializer, OrderSerializer, RatingSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CatelogyViewSet(viewsets.ModelViewSet):
    queryset = Catelogy.objects.all()
    serializer_class = CatelogySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

