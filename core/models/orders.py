from django.db import models


class OrdersBuy(models.Model):
    code_product = models.IntegerField(null=False, blank=False, verbose_name="Código do produto")
    code_branch = models.IntegerField(null=False, blank=False, verbose_name="Código da filial")
    code_provider = models.IntegerField(null=False, blank=False, verbose_name="Código do fornecedor")
    company = models.IntegerField(null=False, blank=False, verbose_name="ID Empresa na Insight")

    quantity_over = models.FloatField(null=False, blank=False, verbose_name="Quantidade de saldo")
    order_number = models.IntegerField(null=False, blank=False, verbose_name="Número do pedido")
    date_order = models.DateField(null=False, blank=False, verbose_name="Data do pedido")

    sent = models.BooleanField(default=False, blank=True, null=True, verbose_name="Enviado ao servidor?")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.code_product
