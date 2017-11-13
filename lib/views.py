from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Author, Book
from .forms import BookForm, AuthorForm


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


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('library:authors')
    form = AuthorForm()
    return render(request, 'lib/author_add.html', {'form': form})


def books(request):
    all_books_list = Book.objects.all()
    context = {'all_books_list': all_books_list}
    return render(request, 'lib/books.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'lib/book_detail.html', {'book': book})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('library:books')
    form = BookForm()
    return render(request, 'lib/book_add.html', {'form': form})


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.POST:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library:books')
    form = BookForm(instance=book)
    context = {'form': form}
    return render(request, 'lib/book_add.html', context)


def update_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.POST:
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('library:authors')
    form = AuthorForm(instance=author)
    context = {'form': form}
    return render(request, 'lib/author_add.html', context)
