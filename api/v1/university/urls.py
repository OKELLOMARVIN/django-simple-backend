from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.university.university_viewset import UniversityViewSet

router = DefaultRouter()
router.register(r'', UniversityViewSet, basename='UniversityViewSet')

urlpatterns = [
    path('', include(router.urls)),
]