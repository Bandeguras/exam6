from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Book
# from webapp.form import TaskForm
# Create your views here.


def index_view(request):
    books = Book.objects.order_by('-completion_at')
    context = {
        'books': books,
    }
    return render(request, 'index.html', context)
