from django.contrib import admin
from library.models import Book, Author, Member, BorrowRecord

# Register your models here.
admin.site.register([
    Author, Book, Member, BorrowRecord
])