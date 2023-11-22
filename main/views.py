from django.shortcuts import render, redirect, get_object_or_404
from main.models import Item
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    
    context = {
        'app': 'player01-inventory',
        'name': request.user.username,
        'class': 'PBP F',
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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

@login_required(login_url='/login')
def add_item_amount(request, id):
    item = get_object_or_404(Item, pk=id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def reduce_item_amount(request, id):
    item = get_object_or_404(Item, pk=id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def delete_item(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')

        try:
            item = Item.objects.get(pk=item_id, user=request.user)
            item.delete()
        except Item.DoesNotExist:
            pass

    return redirect('main:show_main')

def edit_item(request, id):
    # Get item berdasarkan ID
    item = get_object_or_404(Item, pk=id)
    #Item = Item.objects.get(pk = id)

    # Set item sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    # Get data berdasarkan ID
    item = Item.objects.get(pk = id)
    # Hapus data
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def get_item_json(request):
    item_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', item_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        category = request.POST.get("category")
        user = request.user

        new_item = Item(name=name, amount=amount, price=price, description=description, category=category, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request):
    try:
        item = Item.objects.get(pk=item_id)
        item.delete()
        return JsonResponse({'message': 'Item berhasil dihapus.'})
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item tidak ditemukan.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_item = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            description = data["description"],
            category = data["category"]
        )

        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)

# Create your views here.