from django import forms
from .models import Author, Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author',)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)
