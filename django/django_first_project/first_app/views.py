from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #return HttpResponse("Hello world")
    my_dict = {'my_name': "My Name is Ajay R"}
    return render(request, 'first_app/index.html', context=my_dict)
def random(request):
    return HttpResponse("My name is Ajay")

# Create your views here.

