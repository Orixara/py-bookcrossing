from django.contrib import admin

from books.models import Author, Genre, BookListing


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookListing)
