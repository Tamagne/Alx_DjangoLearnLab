from django.urls import path
from django.contrib.auth import views as auth_views
# blog/urls.py
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),  # For listing posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # For viewing individual posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # For creating a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # For editing a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # For deleting a post
]


