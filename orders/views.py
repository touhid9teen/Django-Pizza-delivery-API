from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status

from .models import Order
from .serializers import OrderSerializer
from .authenticate import CustomAuthentication

class OrderListView(APIView):
    authentication_classes = [CustomAuthentication]
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.GET.get('user')
        id = request.GET.get('id')

        if(user and id):
            try:
                order = Order.objects.get(id=id, user=user)
                serializer = OrderSerializer(order)
                return Response(serializer.data)
            except Order.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif(user):
            try:
                order = Order.objects.filter(user=user)
                serializer = OrderSerializer(order, many=True)
                return Response(serializer.data)
            except Order.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = request.data.get('user')
        id = request.data.get('id')

        order = request.data
        data = Order.objects.get(id=id, user=user)
        serializer = OrderSerializer(data, data=order, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.data.get('user')
        id = request.data.get('id')
        data = Order.objects.get(id=id, user=user)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



