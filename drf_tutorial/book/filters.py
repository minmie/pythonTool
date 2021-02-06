from django_filters import rest_framework as filters
from .models import Book


class BookFilter(filters.FilterSet):
    # 这里定义的字段可被用于过滤
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')  # 最低价格 http://127.0.0.1:8000/book?min_price=10
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')  # 最高价格 http://127.0.0.1:8000/book?max_price=10
    # authors__name = filters.CharFilter(lookup_expr='in')
    publish__name = filters.CharFilter(lookup_expr='icontains')  # http://127.0.0.1:8000/book?max_price=10&publish__name=%E5%B7%A5%E4%B8%9A%E5%87%BA%E7%89%88%E7%A4%BE
    publish__address = filters.CharFilter(lookup_expr='exact')  # http://127.0.0.1:8000/book?publish__address=%E7%A6%8F%E5%BB%BA

    authors__name = filters.CharFilter(lookup_expr='icontains')  # http://127.0.0.1:8000/book?authors__name=arvin

    class Meta:
        model = Book
        fields = ['authors', 'title', 'publish']  # 定义要被用来过滤的字段，默认都是完全匹配
