# LibraryProject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include URLs from relationship_app
    path('relationship_app/', include('relationship_app.urls')),
    
    # Add other app URL patterns as needed
]
