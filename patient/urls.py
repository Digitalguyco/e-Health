from .views import addmedicalinfo
from django.urls import path

urlpatterns = [
    path('addmedicalinfo/',addmedicalinfo, name='addmedicalinfo'),
]