from django.urls import path
from . import views

#url namespace
app_name = 'srrt_lib'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:book_id>/',views.detail, name='detail'),
]