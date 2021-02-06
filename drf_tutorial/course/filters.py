from django_filters import rest_framework as filters
from .models import Course


class CourseFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')  # 最低价格 http://127.0.0.1:8000/course/gcbv/list/?min_price=20
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')  # 最高价格 http://127.0.0.1:8000/course/gcbv/list/?max_price=20

    class Meta:
        model = Course
        fields = ['teacher', 'name', 'min_price', 'max_price']