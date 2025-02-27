from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def post_list(request):
    return HttpResponse("Hello, world. You're at the polls list.")

def post_detail(request, pk):
    return HttpResponse(f"Hello, world. You're at the polls detail {pk}.")