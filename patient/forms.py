from django import forms
from .models import MedicalInfo


class MedicalInfoForm(forms.ModelForm):
    class Meta:
        model = MedicalInfo
        fields = ("sex","date_of_birth","disease")
        widgets = {
            "date_of_birth": forms.DateInput(attrs={'type':'date'})
        }
        