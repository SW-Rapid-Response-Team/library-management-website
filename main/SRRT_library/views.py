from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Book, CheckoutLog
from datetime import timedelta
from django.core.paginator import Paginator  
from django.db.models import Q

# Create your views here.
def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')  # 검색어
    category = request.GET.get('category','all')
    book_list = Book.objects.order_by('-subject')
    if category != 'all' and kw != '':
        book_list = book_list.filter(
            Q(kinds_of_books__icontains=category) &
            Q(subject__icontains=kw) 
            ).distinct()
    elif category != 'all' and kw == '':
        book_list = book_list.filter(
            Q(kinds_of_books__icontains=category)
            ).distinct()
    elif category == 'all' and kw != '':
        book_list = book_list.filter(
            Q(subject__icontains=kw) 
            ).distinct()

    paginator = Paginator(book_list, 10)  
    page_obj = paginator.get_page(page)# 페이지당 10개씩 보여주기
    context = {'book_list' : page_obj,'page': page, 'kw': kw,'category':category}
    return render(request, 'SRRT_library/book_list.html',context)

def detail(request, book_isbn):
    book = get_object_or_404(Book, pk=book_isbn)#primary_key
    
    record_exist = 0
    if request.user.is_authenticated:
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