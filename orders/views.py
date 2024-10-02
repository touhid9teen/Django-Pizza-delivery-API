from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from  rest_framework import status
from .models import Order
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer, UserAndOrderDetailSerializer
from .authenticate import CustomAuthentication
from django.core.cache import cache
from django.shortcuts import get_object_or_404

User = get_user_model()

class factorial_with_cache(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self, request,n):

        result = cache.get(f'factorial_{n}')
        if result is None:
            temp = 1
            for i in range(1,n):
                temp *= i
                cache.set(f'factorial_{n}', temp, 60)

            result = cache.get(f'factorial_{n}')
            return JsonResponse({'message' : 'Data does not consist in cash', f'factorial_{n} is' : result})
        return JsonResponse({'message' : 'Data consist in cash', f'factorial_{n} is' : result})


class OrderListView(APIView):
    authentication_classes = [CustomAuthentication]
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            all_data = Order.objects.all()
            cache.delete('order_key')
            cache.set('order_key', all_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        order_id = request.GET.get('id')

        order_data = cache.get('order_key')
        print("order data",order_data)
        if not order_data:
            try:

                order = Order.objects.filter(
                    Q(user=request.user)
                )
                if order_id:
                    order = order.filter(order_id=order_id)
                if not order:
                    return Response({'message' : 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
                serializer = OrderSerializer(order, many=True)
                all_data = Order.objects.all()
                cache.delete('order_key')
                cache.set('order_key', all_data)
                return Response({'error': 'Order not found in cash', 'data': serializer.data})
            except Order.DoesNotExist:
                return Response({'error': 'Order not found'},status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Order found in cash', 'data': order_data}, status=status.HTTP_200_OK)



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
            # orders = Order.objects.select_related('user').filter(user_id=request.user.id)
            # orders = Order.objects.filter(user_id=request.user.id)
            # orders = Order.objects.filter(user_id=request.user.id, order_id='b9875e8e-dca1-4f79-b023-4728386bf340').values('size','order_type')

            # orders = Order.objects.filter(user=request.user).values('size', 'order_type', 'user__username', 'user__email')
            orders = Order.objects.filter(user=request.user).values('size', 'order_type', 'user__username', 'user__email')
            print(orders)
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
        return JsonResponse(list(orders), safe=False)
        # serializer = UserAndOrderDetailSerializer(orders, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.permissions import AllowAny

class OrderListViewV2(APIView):
    permission_class = [AllowAny]

    def get(self, request):
        # cache_key = 'upay_cache_key'
        get_cache = cache.get("upay_cache_key")
        cache.set("upay_cache_key", get_cache)
        print("test__________________", get_cache)
        # i
        # else:
        #     print("get from db________________")
        #     order_list = Order.objects.all()
        #     serializer = OrderSerializer(order_list, many=True)
        #     cache.set(cache_key, serializer.data)
        #     return Response(serializer.data)
        # cache set

    def post(self, request):
        order_data = request.data
        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid():
            serializer.save()
            print("cache delete______________")
            cache.delete('upay_cache_key')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







