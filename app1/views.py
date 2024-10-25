import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import FanLog, FanSpecification
from django.utils.dateparse import parse_datetime


def fan_control(request):
    if request.method == 'POST':
        status = bool(int(request.POST['status']))
        speed_level = int(request.POST['speed_level'])

        # Log the fan control event
        FanLog.objects.create(status=status, speed_level=speed_level)

        return JsonResponse({'message': 'Fan data logged successfully'})

    return render(request, 'fan/fan_control.html')

def calculate_energy(start_time, end_time):
    logs = FanLog.objects.filter(timestamp__range=[start_time, end_time], status=True).order_by('timestamp')

    total_energy = 0.0
    for i in range(1, len(logs)):
        speed_level = logs[i].speed_level
        start = logs[i-1].timestamp
        end = logs[i].timestamp

        duration_hours = (end - start).total_seconds() / 3600

        # Get the current for the speed level
        current = FanSpecification.objects.get(speed_level=speed_level).current
        power = current * 220 * 0.8  # P = IV * Power Factor

        # Energy in Wh
        energy = power * duration_hours
        total_energy += energy

    return total_energy

def energy_consumption(request):
    return render(request, 'fan/energy_consumption.html')

def energy_consumption_calculation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_time_str = data.get('start_time', None)
        end_time_str = data.get('end_time', None)
        start_time_obj = parse_datetime(start_time_str)
        end_time_obj = parse_datetime(end_time_str)
        total_energy = calculate_energy(start_time_obj, end_time_obj)
        return JsonResponse({'total_energy': total_energy})
