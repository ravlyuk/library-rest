from django.shortcuts import render
from rest_framework import generics
from book.serializers import BookSerializer, BookCreateSerializer
from book.models import Book


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookCreateSerializer


class BookAllView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.get_all()


class BookDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookGetByIdView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
