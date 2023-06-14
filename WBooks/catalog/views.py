from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Author, Book, BookInstance


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avialable = BookInstance.objects.filter(status__exact=2).count()
    num_authord = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_avialable': num_instances_avialable,
                           'num_authord': num_authord,
                           'num_visits': num_visits,
                           })


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3


class LoangedBooksUserListView(LoginRequiredMixin, generic.ListView):
    """Представление списка книг, находящихся в заказе у тек.польз"""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 7

    def get_queryset(self):
        return BookInstance.objects.filter(
            borrower=self.request.user).filter(status__exact='2').order_by('due_back')


class AuthorsCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('catalog:authors')


class AuthorsUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('catalog:authors')


class AuthorsDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('catalog:authors')


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('catalog:books')


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('catalog:books')


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('catalog:books')
