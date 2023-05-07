from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView
from patient.models import MedicalInfo
# Create your views here.
class Dashboard(TemplateView):
    template_name = "dashboard.html"
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "medical_practitioner":
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        else:
            return redirect('login')
        
class Patients(TemplateView):
    template_name = 'all_patients.html'


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "medical_practitioner":
            context = self.get_context_data(**kwargs)
            context['patients'] = MedicalInfo.objects.all()
            return self.render_to_response(context)
        else:
            return redirect('login')
    
