from django.urls import path

from . import views

app_name = 'SRRT_library'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:book_isbn>/',views.detail, name = 'detail'),
    path('checkout/<int:book_isbn>/', views.checkout, name='checkout'),
    path('return_book/<int:book_isbn>/', views.return_book, name='return_book'),
    path('my_page/',views.my_page, name='my_page'),
] 