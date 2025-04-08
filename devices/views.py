from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import IoTDevice


def device_list_view(request):
    devices = IoTDevice.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})


def toggle_led(request, device_id):
    device = get_object_or_404(IoTDevice, id=device_id, device_type='LED')

    # Placeholder for actual control logic
    # For example: send MQTT/HTTP command to toggle LED
    print(f"Toggling LED: {device.name}")

    return JsonResponse({'status': 'toggled', 'device': device.name})


def stream_camera(request, device_id):
    device = get_object_or_404(IoTDevice, id=device_id, device_type='CAMERA')

    # You can redirect to camera stream URL or embed it
    return render(request, 'devices/camera_stream.html', {'device': device})
