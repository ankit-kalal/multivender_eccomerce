from django.shortcuts import render,redirect
from django.core.paginator import Paginator

from .forms import ProductForm
from .models import Product
from cart.models import CartItem

# Create your views here.

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('home')
        else:
            print('else===')
            if not form.is_valid():
                for field_name, field_errors in form.errors.items():
                    print(f"Field: {field_name}, Errors: {', '.join(field_errors)}")
                    
            return render(request, 'product/add_product.html', {'form': form})
            

    add_product_form = ProductForm()
    
    return render(request, 'product/add_product.html' ,{'form': add_product_form})


def home(request):
    page_number = request.GET.get('page')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    search = request.GET.get('search')
    category_name = request.GET.get('category_name')

    products = Product.objects.all()

    cart_items = CartItem.objects.filter(user=request.user, order__isnull=True)
    
    if cart_items:
        product_in_cart = sum(item.quantity for item in cart_items)
    else:
        product_in_cart = 0


    if min_price is not None:
        products = products.filter(price__gte=min_price)

    if max_price is not None:
        products = products.filter(price__lte=max_price)

    if category_name:
        products = products.filter(category=category_name)



    products_count = products.count()

    products = Paginator(products, 3)
    products = products.get_page(page_number)

    context = {'products': products,
               'products_count': products_count,
               'product_in_cart' : product_in_cart}

    return render(request, 'home.html',context)
    
