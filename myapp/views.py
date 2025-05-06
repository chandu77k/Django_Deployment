from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Template located in templates/home.html
