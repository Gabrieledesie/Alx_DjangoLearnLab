author_name = "Israel"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)


library_name = "Obj library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

library_name = "Obj library"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)