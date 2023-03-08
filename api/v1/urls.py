
from django.urls import path, include

urlpatterns = [
    path('student/', include('api.v1.student.urls')),
    path('university/', include('api.v1.university.urls')),
]