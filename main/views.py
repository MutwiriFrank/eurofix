import email
from itertools import product
from multiprocessing import context
from django.shortcuts import render
from . models import Dealers, Product, Category, Subscribers_Email
from .filters import DealersFilter
from django.contrib import messages
# Create your views here.

def home(request):
    product = Product.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        Subscribers_Email.objects.create(email=email)
        print(email)
        if email:
            messages.success(request, "Email received. thank You! ")
    context = {
        'products' : 'products',
    }
    return render(request, 'main/home.html',  context = context)

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    products = category.product_set.all()
    context = {
        'category': category,
        'products' : products,
    }

    return render(request, 'main/tile_applications.html',  context = context)

def all_products(request):
    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, 'main/tile_applications.html',  context = context)




def product_page(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        'product' : product,
    }

    return render(request, 'main/product.html',  context = context)


def dealers_page(request):
    all_dealers = Dealers.objects.all()

    myfilter = DealersFilter( request.GET, queryset=all_dealers )
    dealers = myfilter.qs

    context = {
        'dealers' : dealers,
        'myfilter': myfilter,
    }

    return render(request, 'main/dealers.html', context= context)


def about(request):
    return render(request, 'main/about.html')

def subscription(request):
    if request.method == 'POST':
        email = request.POST['email']
        Subscribers_Email.objects.create(email=email)
        print(email)
        if email:
            messages.success(request, "Email received. thank You! ")
        return render(request, 'main/home.html', context= context)