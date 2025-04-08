from django.db import models
from django.utils import timezone

class LocalServer(models.Model):
    """
    Represents this local server (building management unit).
    Used for identifying and syncing with the VPS server.
    """
    hostname = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.GenericIPAddressField()
    registered_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hostname} - {self.ip_address}"


class VPSSyncStatus(models.Model):
    """
    Stores the current sync status with the VPS server.
    Useful for health checks and offline handling.
    """
    local_server = models.OneToOneField(LocalServer, on_delete=models.CASCADE)
    last_synced_at = models.DateTimeField(default=timezone.now)
    success = models.BooleanField(default=False)
    response_code = models.IntegerField(null=True, blank=True)
    error_message = models.TextField(blank=True)

    def __str__(self):
        return f"Sync Status for {self.local_server.hostname} @ {self.last_synced_at}"


class ServerAuthToken(models.Model):
    """
    Optional: Stores a secure token/key for authenticating with the VPS.
    """
    local_server = models.OneToOneField(LocalServer, on_delete=models.CASCADE)
    token = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"AuthToken for {self.local_server.hostname}"
