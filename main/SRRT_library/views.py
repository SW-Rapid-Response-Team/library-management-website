from django.shortcuts import render, get_object_or_404
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
