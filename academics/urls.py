from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseClassViewSet

router = DefaultRouter()
router.register(r'course-classes', CourseClassViewSet, basename='courseclass')

urlpatterns = [
    path('', include(router.urls)),
]
