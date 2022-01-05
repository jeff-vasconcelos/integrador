from django.db import models


class Configuracao(models.Model):
    username = models.CharField(max_length=84, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    empresa = models.CharField(max_length=84, null=True, blank=True)
    empresa_id = models.CharField(max_length=84, null=True, blank=True)

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'

    def __str__(self):
        return self.empresa


class Registro(models.Model):
    message = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return self.message
