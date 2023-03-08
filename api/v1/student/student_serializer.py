from rest_framework import serializers

from api.models import Student, University


class StudentSerializer(serializers.ModelSerializer):
    university = serializers.SlugRelatedField(slug_field='title', queryset=University.objects.all())
    class Meta:
        model = Student
        fields = ['id','name', 'gender', 'age', 'email', 'university']