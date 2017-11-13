from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author',)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)
