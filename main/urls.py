from .views import IndexView, StaticialDetailsView, MedicalPractioners
from django.urls import path

urlpatterns = [
    path('',IndexView.as_view(), name='home'),
    path('users_data/',StaticialDetailsView.as_view(), name='staticaldetails'),
    path('medical_practitioners/',MedicalPractioners.as_view(), name='medicalpractitioners'),
]