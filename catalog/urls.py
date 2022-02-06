from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name="book_detail"),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorListView.as_view(), name="author_detail"),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

]
