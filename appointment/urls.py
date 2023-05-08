from .views import BookAppointmentView,AcceptAppointmentView,RejectAppointmentView,MedicalPractitionerAppointmentListView
from django.urls import path

urlpatterns = [
   path('', MedicalPractitionerAppointmentListView.as_view(), name='medical_practitioner_appointments'),
   path('book/<int:medical_practitioner_id>/', BookAppointmentView.as_view(), name="book_appointment"),
   path('confirm/', AcceptAppointmentView.as_view(), name="appointment_confirmation"),
   path('reject/<int:pk>/', RejectAppointmentView.as_view(), name="reject_appointment"),
   path('accept/<int:pk>/', AcceptAppointmentView.as_view(), name="accept_appointment"),

]