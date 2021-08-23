from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('publications/', views.PublicationView.as_view(), name='publications'),
    path('favorited/', views.FavoritedView.as_view(), name='favorited'),
    path('search_posts/', views.search_posts, name="search_posts"),
    path('create_post/', views.create_post, name="create_post"),
    path('approve_comment/', views.approve_comment, name='approve_comment'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('fav/', views.favorite_view, name='fav'),
    path('<slug:slug>/', views.postDetail, name='post_detail'),
    path('', views.IndexView.as_view(), name="home"),
]
