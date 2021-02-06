from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course import views

router = DefaultRouter()
# basename :是用来拼接urlName 的，默认是模型小写，  别名={basename}-{url_name}
router.register(prefix="viewsets", viewset=views.CourseViewSet, basename='COURSE')

urlpatterns = [
    # Function Based View
    path('fbv/list', views.course_list, name='fbv-list'),   # 这个name 即是url的别名，用于反向解析， 注意：视图集的这个参数并不是代表别名，见最后
    path("fbv/detail/<int:pk>/", views.course_detail, name="fbv-detail"),

    # Class Based View
    path("cbv/list/", views.CourseList.as_view(), name="cbv-list"),
    path("cbv/detail/<int:pk>/", views.CourseDetail.as_view(), name="cbv-detail"),

    # Generic Class Based View   通用类视图
    path("gcbv/list/", views.GCourseList.as_view(), name="gcbv-list"),
    path("gcbv/detail/<int:pk>/", views.GCourseDetail.as_view(), name="gcbv-detail"),

    # DRF viewsets    视图集
    # 方法一
    # path("viewsets/", views.CourseViewSet.as_view(
    #     {"get": "list", "post": "create"}
    # ), name="viewsets-list"),
    # path("viewsets/<int:pk>/", views.CourseViewSet.as_view(
    #     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
    # ), name="viewsets-detail"),

    # 方法二
    path("ddd/", include(router.urls), name='aaa')   # url: course/ddd/viewsets/
                                                     # 这个name 设置的并没啥卵用
]

