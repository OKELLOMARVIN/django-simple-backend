from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.student.student_viewset import StudentViewSet

router = DefaultRouter()
router.register(r'', StudentViewSet, basename='StudentViewSet')

urlpatterns = [
    path('', include(router.urls)),
]