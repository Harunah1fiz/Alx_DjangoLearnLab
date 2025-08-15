from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
#it provides implementations for various crude operation
from rest_framework import viewsets
from .models import Book
# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
