from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Author, Book

def index(request):
    return HttpResponse('Welcome to the library')

def books(request):
    all_books_list = Book.objects.all()
    context = {'all_books_list': all_books_list}
    return render(request, 'lib/books.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'lib/detail.html', {'book': book})
