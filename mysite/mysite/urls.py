from django.conf.urls import patterns, include, url

from django.contrib import admin

from books import views

admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'mysite.views.home', name='home'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^search/', views.search),
	url(r'^delete/', views.delete),
	url(r'^$', views.table),
	url(r'^information/', views.bookinformation),
	url(r'^authorinformation/', views.authorinformation),
	url(r'^add/', views.add),
	url(r'^author/', views.author),
	url(r'^addauthor/', views.add_author),
)