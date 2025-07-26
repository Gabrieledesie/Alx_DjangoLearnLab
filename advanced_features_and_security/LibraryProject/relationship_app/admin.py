from django.contrib import admin
from .models import Author, Book, Library, Librarian, Member

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Shows title and author in admin
    list_filter = ('author',)           # Adds filter sidebar for author

admin.site.register(Author)
admin.site.register(Book, BookAdmin)    # With custom admin settings
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Member)             # ✅ Don't forget to register Member
