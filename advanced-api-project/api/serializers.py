from rest_framework import serializers
from .models import Author,Book
from django.utils import timezone
# BookSerializer serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("publication year cannot be in the future")
        return value
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("title is too short")
        return value

# AuthorSerializer serializes the Author model and includes nested books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to display all related books dynamically
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name','books']


