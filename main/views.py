from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        'app': 'player01-inventory',
        'name': 'Muhammad Ilham Zikri',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)

# Create your views here.
