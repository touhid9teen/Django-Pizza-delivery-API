from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Order(models.Model):

    order_size = (
        ('Large' , 'large'),
        ('Medium' , 'medium'),
        ('Small' , 'small'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField()