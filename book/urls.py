from django.urls import path

from .views import BookListView, BookView, CreateBookView, SearchBookView

urlpatterns = [
    path('', BookListView.as_view(), name='books'),
    path("<uuid:pk>/", BookView.as_view(), name='book'),
    path('new/', CreateBookView.as_view(), name='new_book'),
    path('search/', SearchBookView.as_view(), name='search'),
]
