from django.db import models


class Provider(models.Model):
    code_provider = models.IntegerField(null=False, blank=False, verbose_name="Código do fornecedor")
    description_provider = models.CharField(max_length=255, null=False, blank=False,
                                            verbose_name="Descrição do fornecedor")
    company = models.IntegerField(null=False, blank=False, verbose_name="ID Empresa na Insight")
    cnpj = models.CharField(max_length=255, null=True, blank=True, verbose_name="CNPJ")
    state_registration = models.CharField(max_length=255, null=True, blank=True, verbose_name="Inscrição estadual")

    sent = models.BooleanField(default=False, blank=True, null=True, verbose_name="Enviado ao servidor?")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.description_provider
