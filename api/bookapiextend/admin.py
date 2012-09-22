from django.contrib import admin

from api.bookapiextend.models import Book, BookCategory

admin.site.register(Book)
admin.site.register(BookCategory)
