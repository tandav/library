from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book

def index(request):
    return HttpResponse('Welcome to the library')

def books(request):
    all_books = Book.objects.all()
    output = ', '.join([q.name for q in all_books])
    return HttpResponse(output)

# def books(request):
    # return HttpResponse('List of all books')
