from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from books.models import BookListing


class BookListView(LoginRequiredMixin, generic.ListView):
    model = BookListing
    template_name = "books/book_list.html"


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = BookListing
    template_name = "books/book_detail.html"
    queryset = BookListing.objects.select_related("owner")


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = BookListing
    template_name = "books/book_form.html"
    fields = "__all__"  # temporarily, until I create the forms
    success_url = reverse_lazy("books:book-list")


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = BookListing
    template_name = "books/book_form.html"
    fields = "__all__" # temporarily, until I create the forms


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = BookListing
    success_url = reverse_lazy("books:book-list")
