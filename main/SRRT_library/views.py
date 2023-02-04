from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
    book_list = Book.objects.order_by('-subject')
    context = {'book_list' : book_list}
    return render(request, 'SRRT_library/book_list.html',context)

def detail(request,book_isbn):
    book = get_object_or_404(Book, pk=book_isbn)#primary_key
    context = {'book' : book}
    return render(request, 'SRRT_library/book_detail.html',context)

def checkout(request, book_isbn):
    book = get_object_or_404(Book, pk=book_isbn)
    if(book.count == 0):
        a= 1
        # 0개인데 대출 버튼을 누르면 alert 창이 뜬다.
        # 만약 1개 이상이면 count 값을 1 낮추고 checkout log에 유저와 반납 일자를 기록한다. 
    return redirect('SRRT_library:detail', book_isbn=book.isbn)