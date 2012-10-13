from django.db import models

import logging

class BookCategory(models.Model):
    text = models.TextField(max_length=1024)
    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    '''
    Many to many field example
    '''
class Book(models.Model):
    name = models.CharField(max_length=75)
    book_title=models.CharField(max_length=100, default="book title")
    author=models.CharField(max_length=100, default="author name not set")
    publish_data=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    book_cat = models.ManyToManyField(BookCategory, related_name="book_category", null=True)

    def __unicode__(self):
        return self.name

    #TODO: when add a book to category update total book no under a category

    def save(self, *args, **kwargs):
        try:
            self.name=self.name.lower()
            super(Book, self).save(*args, **kwargs)
        except :
            pass


    @staticmethod
    def is_book_exists(book_id):
        try:
            Book.objects.get(pk=book_id)
            return True
        except :
            return False;


