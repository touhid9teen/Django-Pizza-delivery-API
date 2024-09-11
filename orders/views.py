from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status
from .models import Order
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer, UserAndOrderDetailSerializer
from .authenticate import CustomAuthentication
from django.shortcuts import get_object_or_404

User = get_user_model()
class OrderListView(APIView):
    authentication_classes = [CustomAuthentication]
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        order_id = request.GET.get('id')

        order = Order.objects.filter(
            Q(user=request.user)
        )
        if order_id:
            order = order.filter(order_id=order_id)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)



    def put(self, request):
        user = request.GET.get('user')
        order_id = request.GET.get('id')

        data = Order.objects.get(order_id=order_id, user=request.user)
        serializer = OrderSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        order_id = request.GET.get('id')
        data = Order.objects.get(order_id=order_id, user=request.user)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderDetailView(APIView):
    authentication_classes = [CustomAuthentication]
    def  get (self, request):

        try:
            # Assuming `Order` has a foreign key to `User` named `customer`
            orders = Order.objects.select_related('user').filter(user_id=request.user.id)
            print(orders.query)
            # for order in orders:
            #     print(f"Order ID: {order.order_id}")
            #     print(f"User: {order.user.username} (User ID: {order.user.id})")  # Access related user details
            #     print(f"Size: {order.size}")
            #     print(f"Order Type: {order.order_type}")
            #     print(f"Created At: {order.created_at}")
            #     print(f"Updated At: {order.updated_at}")
            #     print("-" * 40)
            #
            # o = User.objects.select_related('orders').filter(id=user)
            # print(userInfo)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserAndOrderDetailSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)







