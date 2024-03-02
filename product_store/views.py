from django.shortcuts import render,get_object_or_404
from .models import *
from quality.models import *
def Malumot(request, category_slug=None):
    
    
    if category_slug == None:
        products = Product.objects.filter(mavjudmi=True)
    else:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(mavjudmi=True, category=categories)
    context = {
        "store_category": products,
        
    }
    return render(request,"store.html",context)
def Detail(malumot,id):
    stre = Product.objects.get(id=id)
    quality = Add_Quality.objects.all()
 
    context = {
        "store":stre,
        "silver":quality,
        
            

    } 
    return render(malumot,"detail_product.html",context)
        