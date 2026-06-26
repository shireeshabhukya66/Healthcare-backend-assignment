from django.db import models
from patients.models import Patient
from django.contrib.auth.models import User
from doctors.models import Doctor
# Create your models here.

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return f"{self.patient.name} -> {self.doctor.name}"