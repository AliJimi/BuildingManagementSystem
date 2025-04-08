from django.urls import path
from devices.views import device_list_view, toggle_led


app_name = 'devices'

urlpatterns = [
    path('', device_list_view, name='device_list'),
    path('led/<int:device_id>/toggle/', views.toggle_led, name='toggle_led'),
    path('camera/<int:device_id>/stream/', views.stream_camera, name='stream_camera'),
]
