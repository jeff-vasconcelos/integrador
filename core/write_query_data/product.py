from core.models.products import Product


def writer_product(dataframe_products):
    # iterando dataframe
    for index, row in dataframe_products.iterrows():

        # buscando dados existentes
        qs_product = Product.objects.filter(
            code_product=int(row['ode_product'])
        ).first()

        # gravando novos dados
        if not qs_product:
            qs = Product.objects.create(
                code_product=int(row['cod_produto']),
                description_product=str(row['desc_produto']),
                code_provider=int(row['cod_fornecedor']),
                company=int(row['empresa']),
                packaging=str(row['embalagem']),
                quantity_unit_box=float(row['quantidade_un_cx']),
                brand=str(row['marca']),
                net_weight=str(row['peso_liquido']),
                active_principle=str(row['principio_ativo']),
                code_factory=str(row['cod_fabrica']),
                code_ncm=str(row['cod_ncm']),
                code_auxiliary=str(row['cod_auxiliar']),
                code_department=str(row['cod_depto']),
                code_section=str(row['cod_sec']),
                description_department=str(row['desc_departamento']),
                description_section=str(row['desc_secao'])
            )

            qs.save()

        #  atualizando dados existentes
        if qs_product:

            if qs_product.description_product != str(row['desc_produto']) or qs_product.code_provider != int(
                    row['cod_fornecedor']):
                qs_product.description_product = str(row['desc_produto'])
                qs_product.code_provider = int(row['cod_fornecedor'])
                qs_product.sent = False

                qs_product.save()
