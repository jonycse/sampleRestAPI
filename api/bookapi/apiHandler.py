'''
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, throttle, validate
from django.core.exceptions import ObjectDoesNotExist

import logging

from api.bookapi.models import Book, BookCategory

class ApiHandler(BaseHandler):
    allowed_methods = ('GET')
    model = BookCategory

    def read(self, request, cat_id):
        try:
            logging.error("=======GET===============")
            return self.model.objects.get(pk = cat_id)
        except ObjectDoesNotExist:
            return {"error":"not found"}



'''