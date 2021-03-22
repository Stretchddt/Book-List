from django.urls import path
from .views import BookList, CreateBook, UpdateBook, DeleteBook
urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('create/', CreateBook.as_view(), name='create_book'),
    path('update/<str:pk>/', UpdateBook.as_view(), name='update_book'),
    path('delete/<str:pk>/', DeleteBook.as_view(), name='delete_book'),
]