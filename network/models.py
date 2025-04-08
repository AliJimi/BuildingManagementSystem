from django.db import models
from django.utils import timezone

INTERFACE_TYPES = [
    ('ETHERNET', 'Ethernet'),
    ('WIFI', 'WiFi'),
    ('BLUETOOTH', 'Bluetooth'),
]

PROTOCOL_CHOICES = [
    ('WIFI', 'WiFi'),
    ('ETHERNET', 'Ethernet'),
    ('BLUETOOTH', 'Bluetooth'),
]

class NetworkInterface(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., eth0, wlan0, hci0
    interface_type = models.CharField(max_length=20, choices=INTERFACE_TYPES)
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.interface_type})"


class DiscoveredDevice(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)  # e.g., ESP32-LED
    mac_address = models.CharField(max_length=17)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    protocol = models.CharField(max_length=20, choices=PROTOCOL_CHOICES)
    signal_strength = models.IntegerField(blank=True, null=True)  # RSSI for BT/WiFi
    discovered_at = models.DateTimeField(default=timezone.now)
    is_connected = models.BooleanField(default=False)
    interface = models.ForeignKey(NetworkInterface, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name or self.mac_address} via {self.protocol}"
