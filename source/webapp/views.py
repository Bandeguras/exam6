from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Book
from webapp.forms import BookForm
# Create your views here.


def index_view(request):
    books = Book.objects.order_by('-completion_at')
    context = {
        'books': books,
    }

    return render(request, 'index.html', context)


def create_book_view(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, "create.html", {'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            new_book = Book.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                description=form.cleaned_data['description'],
            )
            return redirect('index')
        else:
            return render(request, "create.html", {'form': form})