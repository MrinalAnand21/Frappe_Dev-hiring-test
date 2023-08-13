from rest_framework import viewsets
from .models import Book, Member, Transaction
from .serializers import BookSerializer, MemberSerializer, TransactionSerializer
from django.shortcuts import render, redirect
from .forms import IssueBookForm
import requests
from django.shortcuts import render, redirect
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


def import_books(request):
    if request.method == 'POST':
        num_books = request.POST.get('num_books')
        response = requests.get(
            f'https://frappe.io/api/method/frappe-library?page=2&title=and&num_books={num_books}')
        if response.status_code == 200:
            books_data = response.json().get('message', [])
            for book_data in books_data:
                book = Book.objects.create(
                    title=book_data['title'],
                    authors=book_data['authors'],
                    isbn=book_data['isbn'],
                    # ... other fields ...
                )
            # Redirect to the main page or a success page
            return redirect('index')

    return render(request, 'import_books.html')


def issue_book(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the main page or a success page
            return redirect('index')
    else:
        form = IssueBookForm()

    return render(request, 'issue_book.html', {'form': form})
