from relationship_app.models import Author, Book, Library

# 1. List all books in a specific library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 2. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.book_set.all()

# 3. Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
