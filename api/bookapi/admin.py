from django.contrib import admin

from api.bookapi.models import Book, BookCategory

admin.site.register(Book)
admin.site.register(BookCategory)
