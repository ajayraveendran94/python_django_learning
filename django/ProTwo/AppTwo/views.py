from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>Welcome To the page</em>")
def help(request):
    title = {'title': "Frequently Asked Questions"}
    return render(request, 'app_two/index.html', context=title)