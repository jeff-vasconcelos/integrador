from django.db import models


class Configuracao(models.Model):
    username = models.CharField(max_length=84, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    empresa = models.CharField(max_length=84, null=True, blank=True)
    empresa_id = models.CharField(max_length=84, null=True, blank=True)
    enable_tasks = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'

    def __str__(self):
        return self.empresa
