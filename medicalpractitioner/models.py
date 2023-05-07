from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Profile(models.Model):
    medical_practitioner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.medical_practitioner.first_name
    