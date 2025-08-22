from django.contrib import admin

from books.models import Author, Genre, BookListing


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "country", )
    list_filter = ("country", )
    search_fields = ("full_name", "country", )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


@admin.register(BookListing)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "genre", "owner", "condition")
    list_filter = ("condition", "author", "genre")
    search_fields = ("title", "owner__username", "author__full_name")
    ordering = ("-id",)
