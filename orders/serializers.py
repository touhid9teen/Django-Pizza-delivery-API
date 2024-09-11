from rest_framework import serializers
from authentication.models import User
from authentication.serializers import UserSerializer
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # size = serializers.CharField(max_length=20, default='small')
    # order_type = serializers.CharField(max_length=20, default='pending')

    class Meta:
        model = Order
        fields = ['order_id', 'user', 'size', 'created_at', 'updated_at', 'order_type']


class UserAndOrderDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['id', 'username', 'email', 'phone_number','orders']
