from rest_framework import viewsets, permissions

from api.models import Student
from api.v1.student.student_serializer import StudentSerializer


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer

    def get_queryset(self):
        query = Student.objects.all()
        return query


