from __future__ import unicode_literals
from django.db import models
from ..loginapp.models import Userlog
class UserManager(models.Manager):
    def new_book(self, data):
        return Book.objects.create(title=data['title'], author=data['author'])

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.CharField(max_length=1, default=0)
    user = models.ForeignKey('loginapp.Userlog', related_name="usersrating")
    book = models.ForeignKey('Book', related_name="booksrating")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects = models.Manager()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects = models.Manager()

class UserBook(models.Model):
    user = models.ForeignKey('loginapp.Userlog', related_name="usersbook")
    book = models.ForeignKey('Book', related_name="booksuser")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)