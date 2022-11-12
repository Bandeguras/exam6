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


def update_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(initial={
            'author': book.author,
            'email': book.email,
            'description': book.description,
        })
        return render(request, 'update.html', {'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.author = form.cleaned_data.get('author')
            book.email = form.cleaned_data.get('email')
            book.description = form.cleaned_data.get('description')
            book.save()
            return redirect('index')
        else:
            return render(request, 'update.html', {'form': form})


def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('index')