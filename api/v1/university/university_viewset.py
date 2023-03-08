from rest_framework import viewsets, permissions

from api.models import University
from api.v1.university.university_serializer import UniversitySerializer


# Create your views here.
class UniversityViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UniversitySerializer

    def get_queryset(self):
        query = University.objects.all()
        return query
