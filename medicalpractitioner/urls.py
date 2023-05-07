from .views import Dashboard, Patients
from django.urls import path

urlpatterns = [
    path('dashboard/',Dashboard.as_view(), name='dashboard'),
    path('all-patients/', Patients.as_view(), name="patients")
]