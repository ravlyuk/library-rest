from rest_framework import generics
from authentication.serializers import UserSerializer
from authentication.models import CustomUser
from order.models import Order
from order.serializers import   OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserAllView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.get_all()


class UserDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserGetByIdView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

class OrderUserAllView(APIView):
    def get(self, request, user_id):
        queryset = Order.objects.filter(user_id=user_id)
        serializer_class = OrderSerializer(queryset, many =True)
        return Response(serializer_class.data)




class OrderUserCreateView(APIView):
    def post(self, request, user_id):
        order = OrderSerializer(data=request.data)
        if order.is_valid():
            order.save()
            return Response(order.data)
        return Response(status=201)



class OrderUserUpdateDeleteView(APIView):
    def get_object(self,user_id,pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Response(status=404)

    def get(self,request, user_id,pk):
        order = self.get_object(user_id,pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self,request, pk,user_id, format =None):
        order = self.get_object(user_id,pk)
        serializer = OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk,user_id, format=None):
        order = self.get_object(user_id,pk)
        order.delete()

        return Response(status=204)


