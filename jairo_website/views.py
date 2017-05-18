from django.shortcuts import render

def index(request):
   return render(request, 'jairo_website/index.html')

def about(request):
    return render(request, 'jairo_website/about.html')

def projects(request):
    return render(request, 'jairo_website/projects.html')

def memes(request):
    return render(request, 'jairo_website/memes.html')