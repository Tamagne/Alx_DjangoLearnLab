from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Library
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test
from .decorators import role_required

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def role_required(role):
    def decorator(view_func):
        return user_passes_test(lambda u: u.userprofile.role == role)(view_func)
    return decorator

# relationship_app/views.py

from django.shortcuts import render
from .models import Book, Library

@role_required('Admin')
def admin_view(request):
    # Code for admin view
    return render(request, 'relationship_app/admin_view.html')

@role_required('Librarian')
def librarian_view(request):
    # Code for librarian view
    return render(request, 'relationship_app/librarian_view.html')

@role_required('Member')
def member_view(request):
    # Code for member view
    return render(request, 'relationship_app/member_view.html')
