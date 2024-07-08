from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

def custom_404(request, exception):
    return render(request, '404.html', status=404)


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100
