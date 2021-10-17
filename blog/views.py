from django.views.generic import ListView, DetailView
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


class IndividualPostView(DetailView):
    template_name = "blog/post_detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        context['comment_form'] = CommentForm()
        return context
