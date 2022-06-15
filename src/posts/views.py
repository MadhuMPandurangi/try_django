from django.http import HttpResponse
from django.shortcuts import render

#  Dont Repeat Yourslf = DRY

# Create your views here.
def home_page(request):
    my_title = "Hello there..."
    return render(request, "home.html", {"title": my_title, "my_list":[1,2,3,4,5]})


def posts_home(request):
    my_title = "Hello there..."
    return render(request, "hello_world.html", {"title": my_title})


def about(request):
    return render(request, "about.html", {"title": "About us"})


def contact(request):
    return render(request, "hello_world.html", {"title": "contact us"})
