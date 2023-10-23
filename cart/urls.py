from django.urls import path,include
from . import views


urlpatterns = [
    path("add_to_cart/<int:product_id>", views.add_to_cart , name = 'add_to_cart'), 
    path("remove_to_cart/<int:product_id>", views.remove_to_cart , name = 'remove_to_cart'),
    path("checkout/", views.checkout , name = 'checkout'),
    path("order_history/", views.order_history , name = 'order_history'),

    
    path("cart/", views.cart , name = 'cart'), 
]