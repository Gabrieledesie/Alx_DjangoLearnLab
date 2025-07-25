from relationship_app.models import Author, Book

# Create and save new Author
author = Author.objects.create(name="Edesie Gabriel", age=30)

# Create and save new Book linked to the author
book = Book.objects.create(title="Mastering Django", publication_date="2025-07-25", author=author)

# Fetch and print all authors
print("Authors:")
for a in Author.objects.all():
    print(f"Name: {a.name}, Age: {a.age}")

# Fetch and print all books
print("\nBooks:")
for b in Book.objects.all():
    print(f"Title: {b.title}, Published: {b.publication_date}, Author: {b.author.name}")
