from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import translation

from .models import Book, Loan
from .forms import BookForm
from .forms import RegisterForm

def some_view(request):
    translation.activate('pl')

@login_required
def book_list(request):
    books = Book.objects.all()

    # Filtrowanie:
    query_author = request.GET.get('author', '')
    query_year = request.GET.get('year', '')

    if query_author:
        books = books.filter(author__icontains=query_author)
    if query_year:
        books = books.filter(year=query_year)

    # Wypożyczenia użytkownika
    loans = Loan.objects.filter(user=request.user, returned=False)
    loaned_books = [loan.book.id for loan in loans]

    return render(request, 'books/book_list.html', {
        'books': books,
        'loaned_books': loaned_books,
        'query_author': query_author,
        'query_year': query_year,
    })

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            print(form.errors)  # tylko na czas debugowania
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

@login_required
def loan_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.is_available:
        Loan.objects.create(book=book, user=request.user)
        book.is_available = False
        book.save()
    return redirect('book_list')

@login_required
def return_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    try:
        loan = Loan.objects.get(book=book, user=request.user, returned=False)
    except Loan.DoesNotExist:
        # Jeśli nie jesteś właścicielem wypożyczenia, to cię cofamy
        return redirect('book_list')

    loan.returned = True
    book.is_available = True
    loan.save()
    book.save()
    return redirect('book_list')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'books/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # po rejestracji przekieruj na logowanie
    else:
        form = RegisterForm()
    return render(request, 'books/register.html', {'form': form})
