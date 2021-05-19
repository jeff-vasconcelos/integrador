from django.db import models


class Parametros(models.Model):
    username = models.CharField(max_length=84, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    empresa = models.CharField(max_length=84, null=True, blank=True)
    empresa_id = models.CharField(max_length=84, null=True, blank=True)
    user_db = models.CharField(max_length=84, null=True, blank=True)
    password_db = models.CharField(max_length=84, null=True, blank=True)
    host_db = models.CharField(max_length=84, null=True, blank=True)
    port_db = models.CharField(max_length=84, null=True, blank=True)
    service_db = models.CharField(max_length=84, null=True, blank=True)

    def __str__(self):
        return self.username
