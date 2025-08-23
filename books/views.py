from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from books.forms import BookForm
from books.models import BookListing


class OwnerOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner_id == self.request.user.id

    def handle_no_permission(self):
        from django.http import Http404
        raise Http404

class BookListView(LoginRequiredMixin, generic.ListView):
    model = BookListing
    template_name = "books/book_list.html"
    paginate_by = 12

    def get_queryset(self):
        queryset = BookListing.objects.select_related(
            "author",
            "genre",
            "owner"
        )
        return queryset


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = BookListing
    template_name = "books/book_detail.html"
    queryset = BookListing.objects.select_related("author", "genre", "owner")


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = BookListing
    template_name = "books/book_form.html"
    form_class = BookForm
    success_url = reverse_lazy("books:book-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, OwnerOnlyMixin, generic.UpdateView):
    model = BookListing
    form_class = BookForm
    template_name = "books/book_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class BookDeleteView(LoginRequiredMixin, OwnerOnlyMixin, generic.DeleteView):
    model = BookListing
    success_url = reverse_lazy("books:book-list")
