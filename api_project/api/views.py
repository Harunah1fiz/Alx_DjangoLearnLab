from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
#it provides implementations for various crude operation
from rest_framework import viewsets
from .models import Book
#for permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
  
class BookViewSet(viewsets.ModelViewSet):

    """
    CRUD operations for Book model.

    Authentication:
    - TokenAuthentication is required.
    - Users must include 'Authorization: Token <token>' in headers.

    Permissions:
    - Only authenticated users can access this API.
    - Admin-only endpoints can use IsAdminUser instead.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
