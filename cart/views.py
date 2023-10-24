from django.shortcuts import render,redirect
from .models import CartItem, Order
from product.models import Product
from .forms import OrderForm

# Create your views here.

def add_to_cart(request,product_id):

    cart_item = CartItem.objects.filter(user=request.user, product__id=product_id, order__isnull=True).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        product = Product.objects.get(id=product_id)
        new_cart_item = CartItem(user=request.user, product=product, quantity=1)
        new_cart_item.save()

    return redirect('cart')


def remove_to_cart(request, product_id):

    cart_item = CartItem.objects.filter(user=request.user, product__id=product_id, order__isnull=True).first()

    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity = cart_item.quantity-1
        cart_item.save()
    
    return redirect('cart')


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user, order__isnull=True)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    for cart_item in cart_items:
        cart_item.total = cart_item.quantity*cart_item.product.price

    context = {
        'total_price': total_price,
        'cart_items': cart_items
    }

    return render(request,'cart/cart.html',context)


def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        cart_items = CartItem.objects.filter(user=request.user, order__isnull=True)
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.status = 'pending'
            order.total_price = total_price
            order.save()

            for cart_item in cart_items:
                cart_item.order = order
                cart_item.save()

            return redirect('home')
        

    form = OrderForm()
    context = {
       "form" : form, 
    }
    return render(request,'cart/checkout.html',context)


def order_history(request):
    user_orders = Order.objects.filter(user=request.user)
    orders = []
    for order in user_orders:
        orders.append(order.id)

    cart_items = CartItem.objects.filter(order__id__in=orders)
    
    context = {
       "cart_items" : cart_items, 
    }

    return render(request,'cart/order_history.html',context)


def incoming_orders(request):
    user_products = Product.objects.filter(seller=request.user)
    cart_items = CartItem.objects.filter(product__in=user_products).order_by("order_id")

    context = {
       "cart_items" : cart_items, 
    }

    return render(request,'cart/incoming_order.html',context)


def update_order(request, order_id):
    order_to_update = Order.objects.filter(id=order_id).first()
    order_to_update.status ='shipped'
    order_to_update.save()
    return redirect('incoming_orders')
    