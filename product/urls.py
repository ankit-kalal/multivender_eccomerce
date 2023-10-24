from django.urls import path,include
from . import views


urlpatterns = [
    path("", views.home , name = 'home'),
    path("add_product/", views.add_product , name = 'add_product'), 
    path("view_product/<int:product_id>", views.view_product , name = 'view_product'), 
    path("add_comment/<int:product_id>", views.add_comment , name = 'add_comment'), 

      
]