from django.contrib import admin

from api.bookapiextend.models import Book, BookCategory

from django import forms
from django.forms.util import ErrorList

import logging

class BookForm(forms.ModelForm):
    class Meta:
        model = Book

    def clean(self):
        try:
            book_name = self.cleaned_data['name']
            # form validation, error list required
            if len(book_name)<5:
                self._errors['name']=ErrorList(["Book name should have at least 5 characters"])
        except:
            pass
        return self.cleaned_data


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    search_fields = ['name']


admin.site.register(BookCategory)
admin.site.register(Book, BookAdmin)

