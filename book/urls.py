
from django.contrib import admin
from django.urls import path
from book.apiview import BookListView, ReviewCreateView, BookDetailView #ReviewDetailView

urlpatterns = [
    path('books', BookListView.as_view(), name="books_list"),
    path('books/<int:book_pk>/reviews', ReviewCreateView.as_view(), name="reviews_list"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="books_detail"),
    # path('reviews/<int:pk>/', ReviewDetailView.as_view(), name="reviews_detail"),
]
