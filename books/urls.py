from django.urls import path

from books.views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("book/create/", BookCreateView.as_view(), name="book-create"),
    path("book/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),
    path("book/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]