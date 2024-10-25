from django.urls import path
from . import views

urlpatterns = [
    path('control/', views.fan_control, name='fan_control'),
    path('consumption/', views.energy_consumption, name='energy_consumption'),
    path('consumption/consumption_calculation/', views.energy_consumption_calculation, name='energy_consumption_calculation'),
]
