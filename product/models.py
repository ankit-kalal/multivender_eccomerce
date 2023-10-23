from django.db import models
from django.contrib.auth.models import User 


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('mens_wear', 'Mens Wear'),
        ('ladies_wear', 'Ladies Wear'),
        ('children_wear', 'Children Wear'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
