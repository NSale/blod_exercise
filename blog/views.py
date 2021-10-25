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
        context = self.get_context(request, slug, comment_form=CommentForm())
        return render(request, 'blog/post_detail.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        context = self.get_context(request, slug, comment_form=comment_form)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = context['post']
            comment.save()
            return HttpResponseRedirect(reverse('individual_post', args=[slug]))

        return render(request, 'blog/post_detail.html', context)

    @staticmethod
    def is_stored_post(request, post_id):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get_context(self, request, slug, comment_form):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'tags': post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return context


class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['stored_posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['stored_posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored-posts.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/')
