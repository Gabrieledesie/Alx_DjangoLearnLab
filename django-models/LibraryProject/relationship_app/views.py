from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Book

# ✅ Book list view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ✅ Role check functions (include user authentication check)
def is_admin(user):
    return user.is_authenticated and user.profile.role == 'admin'

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'librarian'

def is_member(user):
    return user.is_authenticated and user.profile.role == 'member'

# ✅ Views based on roles
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
