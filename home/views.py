from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def mission(request):
    return render(request, 'home/mission.html')

def vision(request):
    return render(request, 'home/vision.html')

def objectives(request):
    return render(request, 'home/objectives.html')

def aboutproject(request):
    return render(request, 'home/aboutproject.html')

def helpus(request):
    return render(request, 'home/helpus.html') 
    
