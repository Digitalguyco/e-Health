from .views import IndexView, StaticialDetailsView
from django.urls import path

urlpatterns = [
    path('',IndexView.as_view(), name='home'),
    path('',StaticialDetailsView.as_view(), name='staticaldetails')
]