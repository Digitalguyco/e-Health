from django.shortcuts import render, redirect
from .forms import MedicalInfoForm
# Create your views here.

def addmedicalinfo(request):
    if request.user.is_authenticated and request.user.user_type == 'patient':

        form = MedicalInfoForm()
        if request.method == "POST":
            form = MedicalInfoForm(request.POST)
            if form.is_valid():
                info = form.save(commit=False)
                info.patient = request.user
                info.save()
        
        return render(request, 'medicalinfo.html', {"form":form})
    else:
        return redirect('login')