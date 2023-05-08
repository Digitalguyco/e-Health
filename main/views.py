from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from accounts.models import CustomUser
from medicalpractitioner.models import Profile

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class StaticialDetailsView(ListView):
    template_name = 'staticaldetails.html'
    model = CustomUser

    def get_queryset(self):
        return CustomUser.objects.filter(user_type='patient')
    

class MedicalPractioners(ListView):
    template_name = 'all_medical_practitioners.html'
    model = Profile

    def get_queryset(self):
        return Profile.objects.all()
    