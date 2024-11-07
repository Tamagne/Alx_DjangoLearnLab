# relationship_app/urls.py

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    
    # Additional paths for other views, if needed
    # For example:
    path('list-books/', views.list_books, name='list_books'),
    path('library-detail/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

