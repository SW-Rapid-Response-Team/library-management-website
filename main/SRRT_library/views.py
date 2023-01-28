from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
    book_list = Book.objects.order_by('-subject')
    context = {'book_list' : book_list}
    return render(request, 'SRRT_library/book_list.html',context)

def detail(request,book_isbn):
    book = Book.objects.get(isbn=book_isbn)
    context = {'book' : book}
    return render(request, 'SRRT_library/book_detail.html',context)
