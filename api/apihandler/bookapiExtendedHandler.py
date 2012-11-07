from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, throttle, validate

from api.utility import errorCodes

from api.bookapiextend.models import Book, BookCategory
from api.utility.apiUtility import ApiUtility, Error, Success

import logging
import sys

class BookApiExtendedHandler(BaseHandler):
    allowed_methods = ('GET','POST')
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

            return Error(errorCodes.NOT_FOUND, 'request not found').__dict__()
        except :
            return Error(errorCodes.BAD_REQUEST, 'bad request').__dict__()
            #return Success(True).__dict__()

    #@classmethod
    #def book_cat(self, model):
    #    return model.book_cat.values("text","id")

    def create(self, request):

        try:
            if not attrs.has_key('book_name') or  not attrs.has_key('category_id'):
                return Error(error_codes.BAD_REQUEST, 'Missing parameters').__dict__()

            attrs = self.flatten_dict(request.POST)
            if ApiUtility.get_function_name(request.path)=='add_book':
                book_name =attrs.get('book_name',None)
                cat_id =attrs.get('category_id',None)

                if book_name==None or not cat_id==None:
                    return Error(error_codes.BAD_REQUEST, 'Missing parameters').__dict__()


                book = Book.objects.create(name=book_name)
                book.save()
                book.book_cat.add(cat_id) #m2m field

            return book
        except:
            return Error(errorCodes.BAD_REQUEST, 'bad request').__dict__()