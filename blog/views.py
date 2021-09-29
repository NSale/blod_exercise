from django.shortcuts import render, get_object_or_404
from blog.models import Post

all_posts = Post.objects.all()


# Create your views here.
def index(request):
    sorted_posts = all_posts.order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": sorted_posts,
    })


def posts(request):
    return render(request, "blog/all_posts.html", {
        "posts": all_posts,
    })


def individual_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    tags = identified_post.tags.all()
    return render(request, "blog/post_detail.html", {
        'post': identified_post,
        'tags': tags,
    })
