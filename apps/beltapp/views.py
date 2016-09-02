from django.shortcuts import render, redirect
from .models import Book, Review, UserBook
from django.contrib import messages
from datetime import datetime
from django.db.models import Count
from ..loginapp.models import Userlog
from django.core.urlresolvers import reverse
import bcrypt
def index(request):
	return render(request, 'loginapp/index.html')
def success(request):
	context = {
		'users':Userlog.objects.all(),
		'book':Book.objects.all(),
		'reviews':Review.objects.order_by('-created_at')[:3]
		}
	return render(request, 'beltapp/index.html', context)
def add_review(request, id):
	Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book_id=request.POST['bookid'], user_id=request.session['user'])
	return redirect(reverse('show_book', kwargs={'id':id}))
def add_book(request):
	context={
		'books':Book.objects.all()
	}
	return render(request, 'beltapp/addbook.html', context)
def new_book(request):
	new_book = Book.userManager.new_book(request.POST)
	return redirect('/books')
def new_book_review(request):
	new_book = Book.userManager.new_book(request.POST)
	request.session['book_id'] = new_book.id
	new_review = Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book_id=request.session['book_id'], user_id=request.session['user'])
	return redirect('/books')
def show_book(request, id):
	context = {
		'book':Book.objects.get(id=id),
		'reviews':Review.objects.all()
		}
	return render(request, 'beltapp/divergent.html', context)
def delete_review(request, id):
	review = Review.objects.get(id=id)
	review.delete()
	return redirect(reverse('show_book', kwargs={'id':id}))
def show_user(request, id):
	context = {
		'user':Userlog.objects.get(id=id),
		'reviews':Review.objects.filter(user_id=id),
		'users': Userlog.objects.filter(id=id).annotate(usersratings = Count("usersrating"))
		}
	return render(request, 'beltapp/users.html', context)