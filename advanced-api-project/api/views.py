from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# ===============================
# BOOK API VIEWS
# ===============================
# These views use DRF's generic class-based views for CRUD operations.
# Each view specifies:
#   - queryset: the data source
#   - serializer_class: how data is serialized/deserialized
#   - permission_classes: access control
# Some override perform_create/perform_update to customize save behavior.
# ===============================

# List all books (GET /books/)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # No permission restriction: publicly accessible


# Retrieve a single book by ID (GET /books/<id>/)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # No permission restriction: publicly accessible


# Create a new book (POST /books/)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only logged-in users can create

    # perform_create is a hook that lets us customize object creation.
    # Here, we simply call serializer.save(), but we could also attach
    # request.user or do extra validation if needed.
    def perform_create(self, serializer):
        serializer.save()


# Update an existing book (PUT/PATCH /books/<id>/)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only logged-in users can update

    # perform_update allows customization of object updating.
    # Currently, just saves the serializer.
    def perform_update(self, serializer):
        serializer.save()


# Delete an existing book (DELETE /books/<id>/)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only logged-in users can delete
