import json
import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item

from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    item_count = len(items)
    context = {
        "name": request.user.username,
        "class": "PBP B",
        "items": items,
        "item_count": item_count,
        'last_login': request.COOKIES['last_login'],    
    }
    return render(request, "main.html", context)

# create item
def create_item(request):       
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)


def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data))

def show_json_user(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data))

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='main:login')
def increment_item(request, id):
    if request.method == 'POST':
        product = Item.objects.get(pk=id)
        product.amount += 1
        product.save()
    return redirect('main:show_main')

@login_required(login_url='main:login')
def decrement_item(request, id):
    if request.method == 'POST':
        product = Item.objects.get(pk=id)
        product.amount -= 1
        product.save()
    return redirect('main:show_main')

@login_required(login_url='main:login')
def delete_item(request, id):
    if request.method == 'POST':
        product = Item.objects.get(pk=id)
        product.delete()
    return redirect('main:show_main')


def get_item_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))
    # data = Item.objects.all()
    # return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, price=price, amount=amount, category=category, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


@csrf_exempt
def delete_item_ajax(request, id):
    if request.method == 'DELETE':
        product = Item.objects.get(id=id, user=request.user)
        product.delete()
        return HttpResponse(b"CREATED", status=201)


@csrf_exempt
def increment_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.amount += 1
    item.save()
    return HttpResponse(b"DELETED", status=201)


@csrf_exempt
def decrement_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.amount -= 1
    item.save()
    return HttpResponse(b"DELETED", status=201)


@csrf_exempt
def create_product_flutter(request):
    print(request.method)
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"],
            category = data["category"],
            amount = int(data["amount"]),
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    