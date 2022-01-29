from django.db import models


class EntryProduct(models.Model):
    code_product = models.IntegerField(null=False, blank=False, verbose_name="Código do produto")
    code_branch = models.IntegerField(null=False, blank=False, verbose_name="Código da filial")
    code_provider = models.IntegerField(null=False, blank=False, verbose_name="Código do fornecedor")
    company = models.IntegerField(null=False, blank=False, verbose_name="ID Empresa na Insight")

    quantity_last_entry = models.FloatField(null=False, blank=False, verbose_name="Quantidade da última entrada")
    value_last_entry = models.FloatField(null=False, blank=False, verbose_name="Valor da última entrada")
    date_last_entry = models.DateField(null=False, blank=False, verbose_name="Data da última entrada")

    sent = models.BooleanField(default=False, blank=True, null=True, verbose_name="Enviado ao servidor?")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.code_product
