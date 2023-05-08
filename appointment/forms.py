from django import forms
from django.contrib.admin.widgets import AdminTimeWidget,AdminDateWidget
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [ 'date','time', 'reason']
        widgets = {
            'date': AdminDateWidget(),
            'time': AdminTimeWidget(),
        }