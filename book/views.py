from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from .models import Book


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    template_name = 'books/books.html'
    model = Book
    context_object_name = 'books'
    login_url = 'account_login'


class BookView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'books/book.html'
    model = Book
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'book.special_status'


class CreateBookView(CreateView):
    model = Book
    template_name = 'books/new_book.html'
    fields = "__all__"


class SearchBookView(ListView):
    template_name = 'books/search.html'
    model = Book
    context_object_name = 'books'

    # def get_queryset(self):
    #     query = self.request.GET.get('search')
    #     return Book.objects.filter(
    #         Q(title__icontains=query | Q(author__icontains=query))
    #     )
