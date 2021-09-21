from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all_posts.html")


def individual_post(request, slug):
    return HttpResponse(f'this is {slug}.')