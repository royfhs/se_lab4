from django.contrib import admin
from .models import Author, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('AuthorID','Name','Age')
	# search_fields = ('first_mame','last_name')
	
class BookAdmin(admin.ModelAdmin):
	list_display = ('Title','AuthorID')
	# list_filter = ('publication_date',)
	
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)