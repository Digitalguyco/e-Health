from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


# Create your models here.

class Status(models.Choices):
    ACCEPTED = "accepted"
    PENDING = "pending"
    REJECTED = "rejected"

class Appointment(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments')
    medical_practitioner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointment')
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    status = models.CharField(choices=Status.choices, default="PENDING", max_length=10)
    reason = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.patient} - {self.medical_practitioner}  - "