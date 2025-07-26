from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Israel"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books written by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name '{author_name}'")

# List all books in a specific library
library_name = "Obj library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in the library '{library_name}':")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'")

# Retrieve the librarian for a specific library
try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for the library '{library_name}': {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to the library '{library_name}'")
