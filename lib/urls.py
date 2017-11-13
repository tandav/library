from django.conf.urls import url

from . import views

app_name = 'library'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.books, name='books'),
    url(r'^books/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^edit_book/(?P<book_id>[0-9]+)$', views.update_book, name='edit_book'),
    url(r'^delete_book/(?P<book_id>[0-9]+)$', views.delete_book, name='delete_book'),
    url(r'^authors/$', views.authors, name='authors'),
    url(r'^authors/(?P<author_id>[0-9]+)/$', views.author_detail, name='author_detail'),
    url(r'^add_author/$', views.add_author, name='add_author'),
    url(r'^edit_author/(?P<author_id>[0-9]+)$', views.update_author, name='edit_author'),
    url(r'^delete_author/(?P<author_id>[0-9]+)$', views.delete_author, name='delete_author'),
]
