from django.shortcuts import render, get_object_or_404
import datetime
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket
import random, os, json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def get_basket(user):
#     if user.is_authenticated:
#         return Basket.objects.filter(user=user)
#     else:
#         return []

def get_hot_product():
    # products = Product.objects.all()
    products = Product.objects.filter(is_active=True, category__is_active=True)
    return random.sample(list(products), 1)[0]

def get_same_products(hot_product):
    # same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk) [:3]
    same_products = Product.objects.filter(category=hot_product.category, is_active=True).exclude(pk=hot_product.pk)[:3]

    return same_products

def main(request):
    title = 'главная'
    
    # products = Product.objects.all()[:3]
    products = Product.objects.filter(is_active=True, category__is_active=True)[:3]

    content = {
        'title': title,
        'products': products,
        # 'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', content)
    

def products(request, pk=None, page=1):
    # print(pk)
    title = 'продукты'
    # links_menu = ProductCategory.objects.all()
    links_menu = ProductCategory.objects.filter(is_active=True)
    # basket = []
    # basket = get_basket(request.user)
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)
        # альтернативный вариант получения коризины пользователя
        # _basket = request.user.basket.all()
        # print(f'basket / _basket: {len(_basket)} / {len(basket)}')
    # if pk is not None:
    if pk:
        if pk == 0:
            category = {'pk': 0, 'name': 'все'}
            # products = Product.objects.all().order_by('price')
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            # products = Product.objects.filter(category__pk=pk).order_by('price')
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            # 'basket': basket,
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    # same_products = Product.objects.all()[3:5]
    same_products = get_same_products(hot_product)
    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        # 'basket': basket,
    }
    return render(request, 'mainapp/products.html', content)
    

def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-777-777-7777',
            'email': 'info_yekaterinburg@geekshop.ru',
            'address': 'Близко к центру',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-999-999-9999',
            'email': 'info_vladivostok@geekshop.ru',
            'address': 'Близко к океану',
        },
    ]
    content = {
        'title': title,
        'visit_date':visit_date,
        'locations': locations,
        # 'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', content)

def product(request, pk):
    title = 'продукты'

    links_menu = ProductCategory.objects.filter(is_active=True)
    product = get_object_or_404(Product, pk=pk)

    content = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        # 'basket': get_basket(request.user),

    }
    return render(request, 'mainapp/product.html', content)