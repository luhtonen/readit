from django.contrib import admin
from books.models import Author
from books.models import Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
