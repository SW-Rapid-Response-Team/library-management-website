from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Book, CheckoutLog
from datetime import timedelta

# Create your views here.
def index(request):
    book_list = Book.objects.order_by('-subject')
    context = {'book_list' : book_list}
    return render(request, 'SRRT_library/book_list.html',context)

def detail(request, book_isbn):
    book = get_object_or_404(Book, pk=book_isbn)#primary_key

    entry = CheckoutLog.objects.filter(borrower=request.user, book = book)
    record_exist = entry.count()
    context = {'book' : book, 'record_exist': record_exist}
    
    return render(request, 'SRRT_library/book_detail.html', context)

def checkout(request, book_isbn):
    book = get_object_or_404(Book, pk=book_isbn)
    book.count -= 1
    book.save()

    next_week = timezone.now() + timedelta(days=7)
    checkout_log = CheckoutLog(borrower = request.user, book = book, return_date=next_week)
    checkout_log.save()
    return redirect('SRRT_library:detail', book_isbn=book.isbn)

def return_book(request, book_isbn):
    book = get_object_or_404(Book, pk=book_isbn)
    book.count += 1
    book.save()
    
    checkout_log_list = get_list_or_404(CheckoutLog, borrower=request.user, book = book)#objects.order_by('return_date')
    checkout_log_list[0].delete()
    return redirect('SRRT_library:detail', book_isbn=book.isbn)