from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Course



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.ReadOnlyField(source='teacher.username')  # 外键字段 只读

    class Meta:
        model = Course
        # exclude = ('id', )  # 不展示哪些字段
        # fields = ('id', 'name', 'introduction', 'teacher', 'price', 'created_at', 'updated_at')  # 展示哪些字段
        fields = '__all__'  # 展示所有字段
        depth = 2  # 关联字段的序列化深度
