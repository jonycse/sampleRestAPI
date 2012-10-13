from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, throttle, validate
from django.core.exceptions import ObjectDoesNotExist



import logging
from api.bookapiextend.models import Book, BookCategory

class BookApiExtendedHandler(BaseHandler):
    allowed_methods = ('GET')
    model = Book
    fields=("id","publish_data", "book_title","name","author","book_cat")


    def read(self, request, book_id=None,*args, **kwargs):
        try:
            if "allbook" in request.path:
                return Book.objects.values()

            return {"error":"Error"}
        except ObjectDoesNotExist:
            return {"error":"not found"}