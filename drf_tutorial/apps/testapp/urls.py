from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path, include
urlpatterns = [
    path('hello/', views.hello),
    path('hello2/', views.hello2),
    path('hello3/', views.hello3),
]

