from rest_framework import serializers
from .models import PatientDoctorMapping

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = ['created_by', 'assigned_at']