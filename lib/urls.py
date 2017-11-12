from django.conf.urls import url

from . import views

app_name = 'library'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.books, name='books'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetailView.as_view(), name='book_detail'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^authors/$', views.authors, name='authors'),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='author_detail'),
    url(r'^add_author/$', views.add_author, name='add_author'),
]
