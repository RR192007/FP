from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Book(models.Model):
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    year = models.CharField(max_length=4)
    def __str__(self):
        return self.title

class BorrowedBooks(models.Model):
    book_isbn = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="bookisbn")
    paid = models.BooleanField()
    dateofborrowing = models.DateField()
    returndate = models.DateField()