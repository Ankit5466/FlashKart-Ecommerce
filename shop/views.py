from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products, Contact, Order, OrderUpdate
from django.contrib.auth.models import User
from django.contrib import messages
from math import ceil
import json

def index(request):
    # product = Products.objects.all()
    # print(product)
    # n = len(product)
    # nslides = n//4 + ceil((n/4) - (n//4))
    all_prods = []
    category = Products.objects.values('category', 'id')
    cats = {item['category'] for item in category}
    for cat in cats:
        prod = Products.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        all_prods.append([prod, range(1, nslides), nslides])
    params = {'all_prods': all_prods}
    return render(request, 'shop/index.html', params)

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method == "POST":
        order_Id = request.POST.get('order_Id', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=order_Id, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=order_Id)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates":updates, "items_json":order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request, 'shop/tracker.html')

def searchMatch(query, item):
    if query in item.description.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    all_prods = []
    category = Products.objects.values('category', 'id')
    cats = {item['category'] for item in category}
    for cat in cats:
        prodtemp = Products.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            all_prods.append([prod, range(1, nslides), nslides])
    params = {'all_prods': all_prods, "msg":""}
    if len(all_prods) == 0 or len(query) < 4:
        params = {'msg': "Please enter relevent search"}
    return render(request, 'shop/search.html', params)

def products(request, id):
    # fetch product using id
    products = Products.objects.filter(id=id)
    return render(request, 'shop/products.html', {'products':products[0]})

def checkout(request):
    if request.method =='POST':
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your Order has been place")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')
