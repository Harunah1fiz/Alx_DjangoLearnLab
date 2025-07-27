from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    register_view,
    LoginView,
    LogoutView,
    list_books,  # your FBV
    LibraryDetailView  # your CBV
)

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Auth routes
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
