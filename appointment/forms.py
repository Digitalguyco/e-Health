from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'medical_practitioner', 'date_time', 'reason']
        widgets = {
            'date_time': AdminSplitDateTime(),
        }