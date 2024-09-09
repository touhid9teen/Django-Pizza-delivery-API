from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status

class OrderListView(APIView):
    def get(self, request):
        return Response(data={'message': "Hello There"},status=status.HTTP_200_OK)