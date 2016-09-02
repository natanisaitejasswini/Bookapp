from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
from datetime import datetime
import bcrypt
Email_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
	def first_name(self,first_name):
		if not len(first_name) > 2:
			return(False,"Invalid Firstname") 
		else:
			return(True,first_name)
	def first_name_charcheck(self,first_name):
		if not first_name.isalpha():
			return(False,"Invalid characters")
		else:
			return(True,first_name)
	def last_name(self,last_name):
		if not len(last_name) > 2:
			return(False,"Invalid lastname") 
		else:
			return(True,last_name)
	def reg_email(self,email):
		if not Email_REGEX.match(email):
			return(False,"Invalid email") 
		else:
			return(True,email)
	def birthday(self,birthday):
		bday = birthday
		# Checking empty date field
		if bday == "":
			return(False, "Invalid Birthdate")
		now = datetime.now()
		print now
		
		# comparing datefield with today
		bday_test = datetime.strptime(birthday, '%Y-%m-%d')
		if bday_test > now:
			return(False, "Invalid Birthdate")
		else:
			return(True, birthday)
	def password(self,password):
		if not len(password) > 5:
			return(False,"Invalid password") 
		else:
				# BCRYPT PASSWORD
			password = password.encode()
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())
			return (True, hashed)
	def confirm_password(self,password,confirm_password):
		if not password == confirm_password:
			return(False,"confirm password")
		else:
			return(True,"password confirmed")
  	def log(self,email,password):
  		# print email, password
  		# users = self.all()
  		# for auser in users:
  		# 	print auser.email
  		# print self.filter(email=email)
  		try:
  			user = self.get(email = email)
  			# print user.password
  		except:
  			return (False, "User Does not Exist")
		password = password.encode()
		user_password = user.password.encode()
		print user_password
		if user and bcrypt.hashpw(password, user_password) == user_password:
			return (True, user)
		else:
			return (False, "Password doesnot match")	

class Userlog(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.CharField(max_length=30)
  birthday = models.DateField()
  password = models.CharField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  UserManager = UserManager()
  objects = models.Manager()











