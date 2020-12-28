from rest_framework import generics, mixins, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from book.models import book, review
from book.serializers import BookSerializer, ReviewSerializer
from book.pagination import smallSetPagination

class BookListView(generics.ListCreateAPIView):
    queryset = book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer
    pagination_class = smallSetPagination
    

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer
    # permision_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewCreateView(generics.CreateAPIView):
    queryset = review.objects.all()
    serializer_class = ReviewSerializer
    permision_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        book_pk = self.kwargs.get("book_pk")
        ebook = get_object_or_404(book, pk = book_pk)
        review_author = self.request.user
        review_queryset = review.objects.filter(book=ebook, review_author = review_author)

        if review_queryset.exists():
            raise ValidationError("Oops! You have already reviewed this book")

        serializer.save(book=ebook, review_author = review_author)


# class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = review.objects.all()
#     serializer_class = ReviewSerializer