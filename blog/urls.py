from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('posts/<slug:slug>', views.individual_post, name='individual_post'),
]
