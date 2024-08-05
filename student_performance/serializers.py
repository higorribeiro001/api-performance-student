from rest_framework import serializers
from .models import StudentPerformance

class StudentPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentPerformance
        fields=('__all__')