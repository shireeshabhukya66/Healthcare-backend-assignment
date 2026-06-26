from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            created_by=self.request.user            
        )
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PatientMappingsView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs["patient_id"]

        return PatientDoctorMapping.objects.filter(
            patient_id=patient_id,
            created_by=self.request.user 
        )
    
class MappingDeleteView(generics.DestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            created_by=self.request.user
        )
