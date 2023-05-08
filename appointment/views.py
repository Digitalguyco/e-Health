from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, FormView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from .models import Appointment
from .forms import AppointmentForm
from accounts.models import CustomUser
# Create your views here.
@method_decorator(login_required, name='dispatch')
class MedicalPractitionerAppointmentListView(ListView):
    template_name = 'medical_practitioner_appointments.html'

    def get_queryset(self):
        return Appointment.objects.filter(medical_practitioner=self.request.user)
@method_decorator(login_required, name='dispatch')
class BookAppointmentView(FormView):
    template_name = 'book_appointment.html'
    form_class = AppointmentForm


    def post(self, request, medical_practitioner_id):
        form = self.form_class(request.POST)
        medical_practitioner = get_object_or_404(CustomUser, pk=medical_practitioner_id)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.medical_practitioner = medical_practitioner
            appointment.save()
            return redirect('appointment_confirmation')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class AcceptAppointmentView(View):
    def post(self, request, *args, **kwargs):
        appointment = Appointment.objects.get(id=self.kwargs['pk'])
        appointment.accepted = True
        appointment.save()
        # Send email notification to patient
        # send_mail(
        #     'Appointment accepted',
        #     'Your appointment has been accepted.',
        #     'noreply@example.com',
        #     [appointment.patient.email],
        #     fail_silently=False,
        # )
        return redirect('medical_practitioner_appointments')


@method_decorator(login_required, name='dispatch')
class RejectAppointmentView(View):
    def post(self, request, *args, **kwargs):
        appointment = Appointment.objects.get(id=self.kwargs['pk'])
        appointment.delete()
        # Send email notification to patient
        # send_mail(
        #     'Appointment rejected',
        #     'Your appointment has been rejected.',
        #     'noreply@example.com',
        #     [appointment.patient.email],
        #     fail_silently=False,
        # )
        return redirect('medical_practitioner_appointments')

@method_decorator(login_required, name='dispatch')
class AppointmentConfirmationView(ListView):
    template_name = 'appointment_confirmation.html'
    model = Appointment

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)
        