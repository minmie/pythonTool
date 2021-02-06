from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django_filters import rest_framework as filters
from django.urls import resolve

from course.filters import CourseFilter
from course.permissions import IsOwnerOrReadOnly
from .serializer import CourseSerializer
from .models import Course
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # Django的信号机制
def generate_token(sender, instance=None, created=False, **kwargs):
    """
    创建用户时自动生成Token
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Token.objects.create(user=instance)


"""一、 函数式编程 Function Based View"""

@api_view(["GET", "POST"])
@authentication_classes((BasicAuthentication, SessionAuthentication, TokenAuthentication))  # 只要满足一个就行,优先于setting里面的配置
@permission_classes((IsAuthenticated,))  # 要满足所有的
def course_list(request):
    """
    获取所有课程信息或新增一个课程
    :param request:
    :return:
    """
    if request.method == "GET":
        s = CourseSerializer(instance=Course.objects.all(), many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        s = CourseSerializer(data=request.data)  # 部分更新用partial=True属性
        if s.is_valid():
            s.save(teacher=request.user)
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes((BasicAuthentication, SessionAuthentication, TokenAuthentication))
def course_detail(request, pk):
    """
    获取、更新、删除一个课程
    :param request:
    :param pk:
    :return:
    """
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == "GET":
            s = CourseSerializer(instance=course)
            return Response(data=s.data, status=status.HTTP_200_OK)

        elif request.method == "PUT":
            s = CourseSerializer(instance=course, data=request.data)
            if s.is_valid():
                s.save()
                return Response(data=s.data, status=status.HTTP_200_OK)
            return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


"""二、 类视图 Class Based View"""
"""
同一个类里面只能出现一种请求方法，如只能有一个get
"""

class CourseList(APIView):
    # permission_classes = (IsAuthenticated,)  # settings.py中已设置，此处是多余的

    def get(self, request):
        """
        :param request:
        :return:
        """
        queryset = Course.objects.all()
        s = CourseSerializer(instance=queryset, many=True)  # 这里是instance = xx
        # s = CourseSerializer(instance=queryset.first())
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        :param request:
        :return:
        """
        s = CourseSerializer(data=request.data)  # 这里是data = xx, return前要先调用.is_valid()
        if s.is_valid():
            s.save(teacher=self.request.user)
            # 分别是<class 'django.http.request.QueryDict'> <class 'rest_framework.utils.serializer_helpers.ReturnDict'>
            print(type(request.data), type(s.data))
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    # permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return

    def get(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)

        s = CourseSerializer(instance=obj)
        return Response(s.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)

        s = CourseSerializer(instance=obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""三、 通用类视图 Generic Class Based View"""

class GCourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseFilter

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class GCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)  # 满足所有权限才能访问此视图
    authentication_classes = [SessionAuthentication, BasicAuthentication]  # 只要满一种认证个就可以


"""四、 DRF的视图集viewsets"""


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

    # 定义额外的url
    @action(methods=['GET'], detail=False)
    def get_two(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)

    # url_path: 设置请求的url，本例是 ：/course/ddd/viewsets/cjq2/，不填的话默认是/course/ddd/viewsets/rv/
    @action(methods=['GET'], detail=False, url_name='cjq1', url_path="cjq2")
    def rv(self, request):
        print(self.action)  # rv
        print(self.name)  # Rv
        print(self.get_view_name())  # Rv

        # 注意，urlName 和url_name不一样，  urlName 是指 url的别名，和url_name则是指action()中设置的参数
        # 已知url 获取 urlNmae（格式一般是 {basename}-{url_name}）
        print(resolve(request.path).url_name)  # COURSE-cjq1
        self.reverse_action('cjq1')

        # 已知urlName 获取url(反向解析）
        print(reverse("gcbv-list"))  # /course/gcbv/list/
        print(reverse("gcbv-detail", args=(1,)))  # /course/gcbv/detail/1/
        # print(reverse("viewsets-list"))  # /course/gcbv/detail/1/
        print(reverse("COURSE-cjq1"))  # /course/ddd/viewsets/cjq2/

        # print(reverse("pathName"))
        return Response(data={"msg": 'ok'})
