from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post
from .forms import CommentForm

all_posts = Post.objects.all()


# Create your views here.
class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class Posts(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'


class IndividualPostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'tags': post.tags.all(),
            'comment_form': CommentForm(),
        }
        return render(request, 'blog/post_detail.html', context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('individual_post', args=[slug]))

        context = {
            'post': post,
            'tags': post.tags.all(),
            'comment_form': comment_form,
        }
        return render(request, 'blog/post_detail.html', context)
