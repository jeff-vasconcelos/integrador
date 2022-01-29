from django.db import models


class Product(models.Model):
    code_product = models.IntegerField(null=False, blank=False, verbose_name="Código do produto")
    description_product = models.CharField(max_length=255, null=False, blank=False, verbose_name="")
    code_provider = models.IntegerField(null=False, blank=False, verbose_name="Código do fornecedor")
    company = models.IntegerField(null=False, blank=False, verbose_name="ID Empresa na Insight")

    packaging = models.CharField(max_length=255, null=True, blank=True, verbose_name="Embalagem")
    quantity_unit_box = models.FloatField(null=False, blank=False, verbose_name="Quantidade unidade na caixa")
    brand = models.CharField(max_length=255, null=True, blank=True, verbose_name="Marca")
    net_weight = models.CharField(max_length=255, null=True, blank=True, verbose_name="Peso líquido")
    active_principle = models.CharField(max_length=255, null=True, blank=True, verbose_name="Principio ativo")
    code_factory = models.CharField(max_length=255, null=True, blank=True, verbose_name="Código de fábrica")
    code_ncm = models.CharField(max_length=255, null=True, blank=True, verbose_name="Código NCM")
    code_auxiliary = models.CharField(max_length=255, null=True, blank=True, verbose_name="Código auxiliar")
    code_department = models.CharField(max_length=255, null=True, blank=True, verbose_name="código departamento")
    code_section = models.CharField(max_length=255, null=True, blank=True, verbose_name="Código Seção")
    description_department = models.CharField(max_length=255, null=True, blank=True,
                                              verbose_name="Descrição departamento")
    description_section = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descrição seção")

    sent = models.BooleanField(default=False, blank=True, null=True, verbose_name="Enviado ao servidor?")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.description_product
