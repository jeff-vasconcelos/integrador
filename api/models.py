from django.db import models


class Pedido(models.Model):
    cod_produto = models.IntegerField(blank=False, null=False)
    desc_produto = models.CharField(max_length=255, blank=False, null=False)
    cof_filial = models.IntegerField(blank=False, null=False)
    preco = models.CharField(max_length=255, null=False, blank=False)
    quantidade = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.desc_produto
