from django.urls import path
from . import views
from .feeds import LatestPostFeed

app_name = 'blog'

urlpatterns = [
    path('', views.list, name='posts'),
    path('<slug:slug_post>/', views.detail, name='detail'),
    path('tag/<slug:tag_slug>/', views.list, name='posts_by_tag'),
    path('feed/', LatestPostFeed(), name='post_feed'),
]