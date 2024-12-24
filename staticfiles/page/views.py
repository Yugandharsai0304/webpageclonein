from django.shortcuts import render

# Create your views here.
def webpage(request):
    return render(request,'webpage.html')

# def home(request):
#     return render(request,'home.html')

def course(request):
    return render(request,'course.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def request(request):
    return render(request,'request.html')

def signin(request):
    return render(request,'signin.html')