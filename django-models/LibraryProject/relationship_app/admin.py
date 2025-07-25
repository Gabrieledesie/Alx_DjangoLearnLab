from django.contrib import admin
from .models import Author, Book, Library, Librarian

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # ✅ Removed broken field
    list_filter = ('author',)           # ✅ Now filtering by valid field

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Library)
admin.site.register(Librarian)
