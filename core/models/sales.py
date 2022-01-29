from django.db import models


class SaleProduct(models.Model):
    code_product = models.IntegerField(null=False, blank=False, verbose_name="Código do produto")
    code_branch = models.IntegerField(null=False, blank=False, verbose_name="Código da filial")
    code_provider = models.IntegerField(null=False, blank=False, verbose_name="Código do fornecedor")
    company = models.IntegerField(null=False, blank=False, verbose_name="ID Empresa na Insight")

    quantity_sales = models.FloatField(null=False, blank=False, verbose_name="Quantidade de vendas")
    price_unit = models.FloatField(null=False, blank=False, verbose_name="Preço unitário")
    financial_cost = models.FloatField(null=False, blank=False, verbose_name="Custo fnanceiro")
    client = models.CharField(max_length=255, null=True, blank=True, verbose_name="cliente")
    note_number = models.IntegerField(null=True, blank=True, verbose_name="Número da nota")
    rca = models.CharField(max_length=255, null=True, blank=True, verbose_name="RCA")
    supervisor = models.CharField(max_length=255, null=True, blank=True, verbose_name="Supervisor")
    date_sale = models.DateField(null=False, blank=False, verbose_name="Data da venda")

    sent = models.BooleanField(default=False, blank=True, null=True, verbose_name="Enviado ao servidor?")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return self.code_product
