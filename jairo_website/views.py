from django.shortcuts import render

def index(request):
    return render(request, 'jairo_website/index.html')