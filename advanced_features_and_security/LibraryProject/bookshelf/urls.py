from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.index, name="home" ),
    path("editbooks", views.edit_book, name='editbooks')
]