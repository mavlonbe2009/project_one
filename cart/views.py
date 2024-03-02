from django.shortcuts import render, redirect
from product_store.models import Product
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def cart(request):
    try:
        cart = Cart.objects.get(session_id=_cart_id(request))
        cart_item = CartItem.objects.filter(cart=cart, mavjudmi=True)
    except ObjectDoesNotExist:
        pass
    context = {
        'cart_item':cart_item
    }
    return render(request, 'cart.html', context)
    
    

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(session_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(session_id=_cart_id(request))
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity = 1
        )
        cart_item.save()
    return redirect('add_cart')