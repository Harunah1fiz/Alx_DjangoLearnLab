from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="pass1234")

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create a book
        self.book = Book.objects.create(
            title="Django for Beginners",
            author=self.author,
            publication_year=2022
        )

        # Endpoints
        self.list_url = reverse("book-list")   # Make sure your urls.py names match
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

        # Clients
        self.client = APIClient()
        self.auth_client = APIClient()
        self.auth_client.login(username="testuser", password="pass1234")

    # ==============================
    # TEST LIST VIEW
    # ==============================
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # ==============================
    # TEST CREATE VIEW
    # ==============================
    def test_create_book_authenticated(self):
        data = {"title": "New Book", "author": self.author.id, "publication_year": 2023}
        response = self.auth_client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {"title": "Unauthorized Book", "author": self.author.id, "publication_year": 2023}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ==============================
    # TEST UPDATE VIEW
    # ==============================
    def test_update_book_authenticated(self):
        data = {"title": "Updated Title", "author": self.author.id, "publication_year": 2022}
        response = self.auth_client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    # ==============================
    # TEST DELETE VIEW
    # ==============================
    def test_delete_book_authenticated(self):
        response = self.auth_client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ==============================
    # TEST FILTER, SEARCH, ORDER
    # ==============================
    def test_filter_books_by_year(self):
        response = self.client.get(f"{self.list_url}?publication_year=2022")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Django for Beginners")

    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_url}?search=django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Django for Beginners")

    def test_order_books_by_title(self):
        response = self.client.get(f"{self.list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
