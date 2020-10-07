from rest_framework import serializers
from .models import Order


from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderforUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderforUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


# class OrderCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['user', 'book', 'plated_end_at']


# class OrderCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['user', 'book', 'plated_end_at']
#
#     def validate(self, data):
#         if data['plated_end_at'] == "":
#             raise serializers.ValidationError('field [plated_end_at] does not be empty')
#         return data


