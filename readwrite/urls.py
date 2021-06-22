from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('password_reset/', views.password_reset_view, name="password_reset"),
    path('create_post/', views.create_post, name="create_post"),
    path('post/<id>', views.password_reset_view, name="password_reset"),
    path('<slug:slug>/', views.postDetail, name='post_detail'),
]
