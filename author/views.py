from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from author.serializers import AuthorSerializer, AuthorCreateSerializer
from author.models import Author


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorCreateSerializer


class AuthorAllView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.get_all()


class AuthorDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorGetByIdView(generics.RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
