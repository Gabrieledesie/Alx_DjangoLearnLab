from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')      # Show these columns in admin list view
    list_filter = ('publication_year',)                         # Add filter sidebar by publication year
    search_fields = ('title', 'author')                         # Add search bar for title and author

admin.site.register(Book, BookAdmin)
