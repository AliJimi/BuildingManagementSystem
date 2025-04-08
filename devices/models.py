from django.db import models


DEVICE_TYPES = [
    ('LED', 'LED'),
    ('CAMERA', 'Camera'),
]

class IoTDevice(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.CharField(choices=DEVICE_TYPES, max_length=10)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    mac_address = models.CharField(max_length=17)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.device_type}: {self.name}"

