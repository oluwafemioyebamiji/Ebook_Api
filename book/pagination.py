from rest_framework.pagination import PageNumberPagination

class smallSetPagination(PageNumberPagination):
    page_size = 2