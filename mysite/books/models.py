from django.db import models
	
class Author(models.Model):
	Name = models.CharField(max_length=40,default=1)
	AuthorID = models.CharField(max_length=5,default=1)
	Age = models.CharField(max_length=3,default=1)
	Country = models.CharField(max_length=5,default=1)
	
	def __unicode__(self):
		return self.Name

class Book(models.Model):
	Title = models.CharField(max_length=100,default=1)
	ISBN = models.CharField(max_length=13,default=1)
	AuthorID = models.CharField(max_length=5,default=1)
	Publisher = models.CharField(max_length=5,default=1)
	PublicshDate = models.DateField(blank=True, null=True)
	
	def __unicode__(self):
		return self.Title