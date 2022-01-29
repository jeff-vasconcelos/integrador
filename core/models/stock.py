from django.db import models


class StockProduct(models.Model):
    code_product = models.IntegerField(null=False, blank=False, verbose_name="Código do produto")
    code_branch = models.IntegerField(null=False, blank=False, verbose_name="Código da filial")
    code_provider = models.IntegerField(null=False, blank=False, verbose_name="Código do fornecedor")
    company = models.IntegerField(null=False, blank=False, verbose_name="ID Empresa na Insight")

    general_quantity = models.FloatField(null=False, blank=False, verbose_name="Quantidade geral")
    indemnify_quantity = models.FloatField(null=False, blank=False, verbose_name="Quantidade indenizada")
    reserve_quantity = models.FloatField(null=False, blank=False, verbose_name="Quantidade reservada")
    pending_quantity = models.FloatField(null=False, blank=False, verbose_name="Quantidade pendente")
    block_quantity = models.FloatField(null=False, blank=False, verbose_name="Quantidade bloqueada")
    available_quantity = models.FloatField(null=False, blank=False, verbose_name="Quantidade disponivel")
    sale_price = models.FloatField(null=False, blank=False, verbose_name="Preço de venda")
    last_entry_cost = models.FloatField(null=False, blank=False, verbose_name="Custo última entrada")
    date_stock = models.DateField(null=False, blank=False, verbose_name="Data do estoque")

    sent = models.BooleanField(default=False, blank=True, null=True, verbose_name="Enviado ao servidor?")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'

    def __str__(self):
        return self.code_product
