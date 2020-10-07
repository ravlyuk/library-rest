from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from order.serializers import OrderSerializer
from order.models import Order
from rest_framework import viewsets, permissions


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrderAllView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.get_all()


class OrderDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderGetByIdView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


#  =============== ModelViewSet #  ===============

class OrderModelViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


