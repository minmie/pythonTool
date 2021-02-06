from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = [

]

router = SimpleRouter()
router.register('', views.BookViewSet, basename='book')
urlpatterns += router.urls