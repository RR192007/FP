from django.contrib import admin
from .models import Book, CustomUser, BorrowedBooks
# Register your models here.
admin.site.register(Book)
admin.site.register(CustomUser)
admin.site.register(BorrowedBooks)