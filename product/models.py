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



class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comment_on_product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comment_by_user", on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
