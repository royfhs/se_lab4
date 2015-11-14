from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from .models import *

# Create your views here.
def search(request):
	try:
		author = Author.objects.get(Name=request.GET['q'])
		author_id = author.AuthorID
		books = Book.objects.filter(AuthorID=author_id)
	except:
		tips = "Sorry, There is no book that you are looking for."
		return render(request,'table.html',{'tips':tips})
	return render(request,'table.html',{'books':books})

def delete(request):
	Book.objects.filter(id=request.GET['i']).delete()
	books = Book.objects.all()
	return render(request,'table.html',{'books':books})

def table(request):
	books = Book.objects.all()
	return render(request,'table.html',{'books':books})

def bookinformation(request):
	x = Book.objects.get(Title=request.GET['Name'])
	return render(request,'bookinformation.html',{'x':x})

def authorinformation(request):
	x = Author.objects.get(Name=request.GET['Name'])
	return render(request,'authorinformation.html',{'x':x})

def add(request):	
	if request.GET['title1'] and request.GET['ISBN1'] and request.GET['ID1'] and request.GET['publisher1']:
		if Author.objects.filter(AuthorID=request.GET['ID1']):
			p = Book(Title = request.GET['title1'],
					ISBN = request.GET['ISBN1'],
					AuthorID = request.GET['ID1'],
					Publisher = request.GET['publisher1'],
					# PublishDate = request.GET['publishdate1']
				)
			p.save()
		else:
			tips = "Add the author first, plz."
			return render(request,'table.html',{'tips':tips})
	else:
		tips = "Input Legal Data, Plz."
		return render(request,'table.html',{'tips':tips})
	books = Book.objects.all()
	return render(request,'table.html',{'books':books})
	
def add_author(request):
	if request.GET['name1'] and request.GET['age1'] and request.GET['ID1'] and request.GET['country1']:
		if Author.objects.filter(AuthorID=request.GET['ID1']):
			raise Http404()
		else:
			p = Author(Name = request.GET['name1'],
					Age = request.GET['age1'],
					AuthorID = request.GET['ID1'],
					Country = request.GET['country1'],
				)
			p.save()
	else:
		tips = "Input Legal Data, Plz."
		return render(request,'table.html',{'tips':tips})
	authors = Author.objects.all()
	return render(request,'author.html',{'authors':authors})

def author(request):
	authors = Author.objects.all()
	return render(request,'authorlist.html',{'authors':authors})