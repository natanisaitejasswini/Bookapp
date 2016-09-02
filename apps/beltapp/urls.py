from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^books$', views.success),
	url(r'^books/add$', views.add_book),
	url(r'^add_review/(?P<id>\d+)$', views.add_review),
	url(r'^new_book$', views.new_book, name='new_book'),
	url(r'^new_book_review$', views.new_book_review, name='new_book_review'),
	url(r'^book/(?P<id>\d+)$', views.show_book, name='show_book'),
	url(r'^delete_review/(?P<id>\d+)$', views.delete_review, name='delete_review'),
	url(r'^users/(?P<id>\d+)$', views.show_user, name='show_user'),
]