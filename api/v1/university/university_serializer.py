from rest_framework import serializers

from api.models import University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id','title', 'code']