from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'ilham',
        'class': 'tugas2'
    }

    return render(request, "main.html", context)

# Create your views here.
