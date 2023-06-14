from django.urls import path, re_path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^authors/create/$', views.AuthorsCreate.as_view(), name='authors_create'),
    re_path(r'^authors/update/(?P<pk>\d+)$', views.AuthorsUpdate.as_view(), name='authors_update'),
    re_path(r'^authors/delete/(?P<pk>\d+)$', views.AuthorsDelete.as_view(), name='authors_delete'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]

urlpatterns += [
    re_path(r'^mybooks/$', views.LoangedBooksUserListView.as_view(), name='my-borrowed'),
    re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    re_path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]
