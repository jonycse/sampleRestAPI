from django.db import models

class BookCategory(models.Model):
    text = models.TextField(max_length=1024)
    def __unicode__(self):
        return self.text

class Book(models.Model):
    name = models.CharField(max_length=75)
    book_title=models.CharField(max_length=100, default="book title")
    author=models.CharField(max_length=100, default="author name not set")
    publish_data=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    book_cat = models.ForeignKey(BookCategory, related_name="puzzle_questions")
    def __unicode__(self):
        return self.name

    #TODO: when add a book to category updade total book no under a category
    #TODO: need to override save method

