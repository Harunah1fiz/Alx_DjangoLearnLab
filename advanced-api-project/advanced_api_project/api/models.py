from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    # Relationship: each book belongs to one author
    # related_name="books" allows accessing books from the Author side (author.books.all())
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='author')