from django.shortcuts import render
from .models import Product, Order, OrderItem
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def store(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {'products': products})

from django.shortcuts import get_object_or_404

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product_detail.html', {'product': product})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('store')

@login_required
def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)

    # Get or create active order
    order, created = Order.objects.get_or_create(
        user=request.user,
        complete=False
    )

    # Get or create order item
    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product
    )

    # If already exists, increase quantity
    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('cart')

@login_required
def cart(request):
    order, created = Order.objects.get_or_create(
        user=request.user,
        complete=False
    )

    items = order.orderitem_set.all()

    return render(request, 'store/cart.html', {
        'order': order,
        'items': items
    })

@login_required
def update_item(request, pk, action):
    product = Product.objects.get(id=pk)
    order = Order.objects.get(user=request.user, complete=False)
    order_item = OrderItem.objects.get(order=order, product=product)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return redirect('cart')

@login_required
def checkout(request):
    order = Order.objects.get(user=request.user, complete=False)

    order.complete = True
    order.save()

    return render(request, 'store/checkout_success.html')
