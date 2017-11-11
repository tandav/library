from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book

def index(request):
    return HttpResponse('Welcome to the library')

def books(request):
    all_books_list = Book.objects.all()
    context = {'all_books_list': all_books_list}
    return render(request, 'lib/books.html', context)

def book_detail(request, book_id):
    return HttpResponse('Detailed view for book {}'.format(book_id))
