from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('countries/',views.countries,name='countries'),
    path('statistics/',views.statistics,name='statistics'),
]