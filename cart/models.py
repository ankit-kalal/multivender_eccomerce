from django.db import models
from product.models import Product

from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    shipping_address = models.TextField()
    city = models.CharField(max_length=255,default="")
    state = models.CharField(max_length=255,default="")
    postal_code = models.IntegerField(default=0)
    country = models.CharField(max_length=255,default="")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
