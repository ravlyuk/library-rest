from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'authors']

    def validate(self, data):
        if data['name'] == "":
            raise serializers.ValidationError('field [Name] does not be empty')
        return data


