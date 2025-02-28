from django.http import HttpResponse, Http404
from django.shortcuts import render

from . models import Post


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def post_list(request):
    posts = Post.published.all()
    context = {
        'posts': posts,
    }
    return render(request, 'template.html', context)


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except:
        raise Http404("Post not found")
    context = {
        'post': post,
    }
    return render(request, 'template2.html', context)
