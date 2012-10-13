from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, throttle, validate
from django.core.exceptions import ObjectDoesNotExist

from api.utility import apiUtility


import logging
from api.bookapiextend.models import Book, BookCategory
from api.utility.apiUtility import ApiUtility

class BookApiExtendedHandler(BaseHandler):
    allowed_methods = ('GET')
    model = Book
    fields=("id","publish_data", "book_title","name","author","book_cat")


    def read(self, request,*args, **kwargs):
        try:
            logging.error(request.path)

            if ApiUtility.get_function_name(request.path)=='allbook':
                return Book.objects.all()

            if ApiUtility.get_function_name(request.path)=='category':
                #return Book.objects.filter(book_cat__text = 'child').values("name","id","book_title")
                return Book.objects.filter(book_cat__pk = kwargs['cat_id']).values("name","id","book_title")

            if ApiUtility.get_function_name(request.path)=='category_name':
                return Book.objects.filter(book_cat__text = kwargs['cat_name'] ).values("name","id","book_title")
                #return Book.objects.filter(book_cat__pk = kwargs['cat_id']).values("name","id","book_title")


            return {"error":"request not found"}
        except ObjectDoesNotExist:
            return {"error":"bad request"}