import uuid
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Order(models.Model):

    order_size = (
        ('Large' , 'large'),
        ('Medium' , 'medium'),
        ('Small' , 'small'),
    )

    order_type = (
        ('Pending' , 'pending'),
        ('On delivery' , 'on delivery'),
        ('delivered' , 'delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=order_size, default=order_size[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_type = models.CharField(max_length=20, choices=order_type, default=order_type[0][0])
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        indexes =[
            models.Index(fields=['order_id']),
        ]

    def __str__(self):
        return  f'< Order is {self.size} is created at {self.created_at} by {self.user}>'
