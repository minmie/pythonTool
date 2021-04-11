from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.throttling import UserRateThrottle

from .serializer import Book
from rest_framework import status, generics, viewsets, throttling
from .serializer import BookSerializer
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import BookFilter

import random
class RandomRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1
# Create your views here.




class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = ()  # 为空代表不需要认证
    permission_classes = ()  # 为空代表不需要检查权限
    # filter_backends = (DjangoFilterBackend,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = BookFilter


    # 搜索
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    search_fields = ['title', 'authors__name', 'publish__name']  # http://127.0.0.1:8000/book?search=%E5%B7%A5%E4%B8%9A%E5%87%BA%E7%89%88

    # 排序
    # https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
    ordering_fields = ['price']  #  http://127.0.0.1:8000/book?ordering=-price
    ordering = ['price']  # 如果设置了这个字段，这个字段是默认排序

    # LimitOffsetPagination
    # PageNumberPagination