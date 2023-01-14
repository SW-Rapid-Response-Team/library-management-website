from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    book_list = Book.objects.order_by('-subject')
    context = {'book_list':book_list}
    return render(request, 'srrt_lib/book_list.html',context)    
    #return HttpResponse("Hi. hello world?aaaa")

def detail(request, book_id):
    book = get_object_or_404(Book,pk=book_id)#Book.objects.get(id=book_id)
    context = {'book':book}
    return render(request,'srrt_lib/book_detail.html',context)
