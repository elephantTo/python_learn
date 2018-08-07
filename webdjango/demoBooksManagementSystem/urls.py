from django.urls import path
from . import views

urlpatterns = [
    path('bookManager',views.index,name='index'),
    path('bookManager/addBook',views.addBook,name='addBook'),
    #re_path('bookManager/bookDetail/(?P<book_id>\d+)/',views.bookDetail,name='bookDetail'),
    path('bookManager/bookDetail/<int:book_id>/',views.bookDetail,name='bookDetail'),
    path('bookManager/deleteBook',views.deleteBook,name='deleteBook'),
]
