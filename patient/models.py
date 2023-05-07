from django.db import models
from accounts.models import CustomUser

# Create your models here.

# Sex Choices
class Sex(models.Choices):
    MALE = "male"
    FEMALE = "female"
 
class MedicalInfo(models.Model):
    patient = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    sex = models.CharField(max_length=100, null=True, blank=True, choices=Sex.choices)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    disease = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.patient.first_name
    
