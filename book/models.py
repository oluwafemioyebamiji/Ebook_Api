from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    author = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class review(models.Model):
    book = models.ForeignKey(book, on_delete = models.CASCADE, related_name = "reviews")
    review_author = models.ForeignKey(User, on_delete= models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(validators =[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.comment} by {self.review_author}"