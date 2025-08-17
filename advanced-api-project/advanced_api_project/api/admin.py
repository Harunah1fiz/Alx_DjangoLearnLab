from django.contrib import admin
from .models import Book, Author
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author","publication_year")   # show these fields in list view
    search_fields = ("title",)                               # add search bar
    list_filter = ("publication_year", "author") 

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)