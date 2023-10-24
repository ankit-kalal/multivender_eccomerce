from django.urls import path,include
from . import views


urlpatterns = [
    path("add_to_cart/<int:product_id>/", views.add_to_cart , name = 'add_to_cart'), 
    path("remove_to_cart/<int:product_id>/", views.remove_to_cart , name = 'remove_to_cart'),
    path("checkout/", views.checkout , name = 'checkout'),
    path("order_history/", views.order_history , name = 'order_history'),
    path("incoming_orders/", views.incoming_orders , name = 'incoming_orders'),
    path("update_order/<int:order_id>/", views.update_order , name = 'update_order'),


    

    

    
    path("cart/", views.cart , name = 'cart'), 
]