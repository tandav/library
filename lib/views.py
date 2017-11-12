from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Author, Book
from .forms import AddBookForm, AddAuthorForm


def index(request):
    return HttpResponse('Welcome to the library')


def authors(request):
    all_authors_list = Author.objects.all()
    context = {'all_authors_list': all_authors_list}
    return render(request, 'lib/authors.html', context)


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('library:authors')
    form = AddAuthorForm()
    return render(request, 'lib/author_edit.html', {'form': form})


def books(request):
    all_books_list = Book.objects.all()
    context = {'all_books_list': all_books_list}
    return render(request, 'lib/books.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('library:books')
    form = AddBookForm()
    return render(request, 'lib/book_edit.html', {'form': form})


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'lib/book_detail.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'lib/author_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['books'] = Book.objects.filter(author_id=self.kwargs['pk'])
        return context        
