from rest_framework import serializers
from book.models import book, review


class ReviewSerializer(serializers.ModelSerializer):

    review_author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = review
        exclude = ("book",)
     


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only = True)
    class Meta:
        model = book
        fields = "__all__"
