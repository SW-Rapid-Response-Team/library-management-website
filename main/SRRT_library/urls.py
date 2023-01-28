from django.urls import path

from . import views

app_name = 'srrt_library'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:book_isbn>/',views.detail, name='detail'),
]