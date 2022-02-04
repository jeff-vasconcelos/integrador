from core.models.sales import SaleProduct


def writer_sale(dataframe_sales):
    # iterando dataframe
    for index, row in dataframe_sales.iterrows():
        print("ENTRO NA FUNÇÃO")

        # buscando dados existentes
        qs_sale = SaleProduct.objects.filter(
            code_product=int(row['cod_produto']),
            code_branch=int(row['cod_filial']),
            code_provider=int(row['cod_fornecedor']),
            quantity_sales=float(row['qt_venda']),
            price_unit=float(row['preco_unit']),
            financial_cost=float(row['custo_fin']),
            date_sale=row['data']
        ).first()

        # gravando novos dados
        if not qs_sale:
            print("SALVANDO VENDAS AGORA")
            print(int(row['cod_produto']))
            qs = SaleProduct.objects.create(
                code_product=int(row['cod_produto']),
                code_branch=int(row['cod_filial']),
                code_provider=int(row['cod_fornecedor']),
                company=int(row['empresa']),
                quantity_sales=float(row['qt_venda']),
                price_unit=float(row['preco_unit']),
                financial_cost=float(row['custo_fin']),
                client=str(row['cliente']),
                note_number=int(row['num_nota']),
                rca=str(row['rca']),
                supervisor=str(row['supervisor']),
                date_sale=row['data']
            )

            qs.save()
