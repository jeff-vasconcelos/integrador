from django.db import models


class Configuration(models.Model):
    username = models.CharField(max_length=84, null=True, blank=True, verbose_name="Usuário Insight")
    password = models.CharField(max_length=128, null=True, blank=True, verbose_name="Senha Insight")
    company = models.CharField(max_length=84, null=True, blank=True, verbose_name="Descrição da Empresa")
    company_id = models.CharField(max_length=84, null=True, blank=True, verbose_name="ID empresa - Insight")
    db_user = models.CharField(max_length=84, null=True, blank=True, verbose_name="Usuário do BD")
    db_password = models.CharField(max_length=84, null=True, blank=True, verbose_name="Senha do BD")
    db_service = models.CharField(max_length=84, null=True, blank=True, verbose_name="Service do BD")
    enable_tasks = models.BooleanField(default=False, null=True, blank=True, verbose_name="Habilitar tarefas?")

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'

    def __str__(self):
        return self.company
