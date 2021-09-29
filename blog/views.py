from datetime import date
from django.shortcuts import render
from blog.models import Post

all_posts = Post.objects.all()


# Create your views here.
def index(request):
    return render(request, "blog/index.html", {
        "posts": all_posts,
    })


def posts(request):
    return render(request, "blog/all_posts.html", {
        "posts": all_posts,
    })


def individual_post(request, slug):
    identified_post = next(post for post in all_posts if post.slug == slug)
    return render(request, "blog/post_detail.html", {
        # 'post': get_post(slug),
        'post': identified_post,
    })
