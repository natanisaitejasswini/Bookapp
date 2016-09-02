from django.shortcuts import render,redirect, HttpResponse
from .models import Userlog
from ..beltapp.models import Review
from ..beltapp.models import Book
from ..beltapp.models import UserBook
from django.contrib import messages
from datetime import datetime
import bcrypt
def user(request):
	errors = False
	check1 = Userlog.UserManager.first_name(request.POST['first_name'])
	check1_char = Userlog.UserManager.first_name_charcheck(request.POST['first_name'])
	check2 = Userlog.UserManager.last_name(request.POST['last_name'])
	check3 = Userlog.UserManager.reg_email(request.POST['email'])
	check4 = Userlog.UserManager.password(request.POST['password'])
	check6 = Userlog.UserManager.birthday(request.POST['birthday'])
	print request.POST['password'] 
	print bcrypt.gensalt()  
	check5 = Userlog.UserManager.confirm_password(request.POST['password'],request.POST['confirm_password'])
	if check1[0] == False:
		messages.add_message(request, messages.INFO, "Invalid firstname", extra_tags="regtag")
		errors = True
	if check1_char[0] == False:
		messages.add_message(request, messages.INFO, "Invalid characters in firstname", extra_tags="regtag")
		errors = True
	if check2[0] == False:
		messages.add_message(request, messages.INFO, "Invalid lastname", extra_tags="regtag")
		errors = True
	if check3[0] == False:
		messages.add_message(request, messages.INFO, "Invalid Email", extra_tags="regtag")
		errors = True
	if check4[0] == False:
		messages.add_message(request, messages.INFO, "Invalid password", extra_tags="regtag")
		print check4[1]
		errors = True
	if check5[0] == False:
		messages.add_message(request, messages.INFO, "Please confirm your password correctly", extra_tags="regtag")
		errors = True
	if check6[0] == False:
		print check6[1]
		messages.add_message(request, messages.INFO, "Invalid BirthDate", extra_tags="regtag")
		errors = True
	# To check DB whether Email already registered or not....
	if Userlog.objects.filter(email = request.POST['email']):
	    messages.add_message(request, messages.INFO, "This email already existed!", extra_tags="regtag")
	    errors = True
	# Errors Route
	if errors == True:
		return redirect('/')
	elif (check1[0] == True & check2[0] == True & check3[0] == True & check4[0] == True & check5[0] == True & check6[0] == True):
		user = Userlog.UserManager.create(first_name=check1[1], last_name=check2[1], email=check3[1], birthday=check6[1], password=check4[1])
		request.session['user'] = user.id
		# messages.add_message(request, messages.INFO, "Successfully Registered", extra_tags="regtag")
		return redirect('/books')

def login(request):
	check7 = Userlog.UserManager.log(request.POST['email'], request.POST['password'])
	if check7[0] == False:
		messages.add_message(request, messages.INFO, check7[1], extra_tags='logtag')
		print check7[1]
		return redirect('/')
	else:
		request.session['user'] = check7[1].id
		# messages.add_message(request, messages.INFO, "Successfully logged in!", extra_tags="regtag")
		return redirect('/books')

def logout(request):
	del request.session['user']
	return redirect('/')







