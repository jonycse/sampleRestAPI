This is sample rest API using django(https://docs.djangoproject.com/) and django-piston (https://bitbucket.org/jespern/django-piston/).


1. Install python 2.7+
2. Install pip first : http://jpython.blogspot.com/search/label/pip
3. pip install django
4. pip install django-piston



Running the project:
    - python manage.py syncdb
    - python manage.py runserver


Some API call example:

Book API:

http://127.0.0.1:8000/myapi/getbook/1/
http://127.0.0.1:8000/myapi/getbook/1/xml/

http://127.0.0.1:8000/myapi/allbook/
http://127.0.0.1:8000/myapi/allbook/xml/

http://127.0.0.1:8000/myapi/category/1/
http://127.0.0.1:8000/myapi/category/1/xml/

*Book API(Extended):*

http://127.0.0.1:8000/myapi/extend/allbook/
http://127.0.0.1:8000/myapi/extend/allbook/xml/