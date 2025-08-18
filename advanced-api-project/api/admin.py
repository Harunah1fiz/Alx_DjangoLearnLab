from django.contrib import admin
from .models import Book, Author
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author","publication_year")   # show these fields in list view
    search_fields = ("title",)                               # add search bar
    list_filter = ("publication_year", "author") 
    

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
