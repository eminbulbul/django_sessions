# from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'sayfa'


class LargePageNumberPagination(PageNumberPagination):
    page_size = 5
    # page_query_param = 'sayfa'