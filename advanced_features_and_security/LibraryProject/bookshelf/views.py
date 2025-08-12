from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def edit_book(request):
    books = Book.objects.all()
    print(request.user.username)
    return HttpResponse(f"you have access {books}")

def index(request):
    return render(request, 'index.html')


