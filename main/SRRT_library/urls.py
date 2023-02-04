from django.urls import path

from . import views

app_name = 'SRRT_library'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:book_isbn>/',views.detail, name = 'detail'),
    path('checkout/<int:book_isbn>/',views.checkout, name='checkout')
]