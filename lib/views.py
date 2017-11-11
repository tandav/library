from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Author, Book

def index(request):
    return HttpResponse('Welcome to the library')

def authors(request):
    all_authors_list = Author.objects.all()
    context = {'all_authors_list': all_authors_list}
    return render(request, 'lib/authors.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author_id=author_id)
    return render(request, 'lib/author_detail.html', {'author': author, 'books': books})

def books(request):
    all_books_list = Book.objects.all()
    context = {'all_books_list': all_books_list}
    return render(request, 'lib/books.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'lib/book_detail.html', {'book': book})
