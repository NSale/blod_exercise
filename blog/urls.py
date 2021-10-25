from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts', views.Posts.as_view(), name='posts'),
    path('posts/<slug:slug>', views.IndividualPostView.as_view(), name='individual_post'),
    path('read-later', views.ReadLaterView.as_view(), name='read-later'),
]
