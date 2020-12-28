from rest_framework import permissions

class IsAdminUserOrReadOnly(permisions.IsAdminUser):
    