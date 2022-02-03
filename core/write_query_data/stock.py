from core.models.stock import StockProduct


def writer_stock(dataframe_stock):
    # iterando dataframe
    for index, row in dataframe_stock.iterrows():

        # buscando dados existentes
        qs_stock = StockProduct.objects.filter(
            code_product=int(row['cod_produto']),
            code_branch=int(row['cod_filial']),
            code_provider=int(row['cod_fornecedor'])
        ).first()

        #  atualizando dados existentes
        if qs_stock:

            qs_stock.general_quantity = float(row['qt_geral']),
            qs_stock.indemnify_quantity = float(row['qt_indenizada']),
            qs_stock.reserve_quantity = float(row['qt_reservada']),
            qs_stock.pending_quantity = float(row['qt_pendente']),
            qs_stock.block_quantity = float(row['qt_bloqueada']),
            qs_stock.available_quantity = float(row['qt_disponivel']),
            qs_stock.sale_price = float(row['preco_venda']),
            qs_stock.last_stock_cost = float(row['custo_ult_entrada']),
            qs_stock.date_stock = row['data'],
            qs_stock.sent = False

            qs_stock.save()

        # gravando novos dados
        else:
            qs = StockProduct.objects.create(
                code_product=int(row['cod_produto']),
                code_branch=int(row['cod_filial']),
                code_provider=int(row['cod_fornecedor']),
                general_quantity=float(row['qt_geral']),
                indemnify_quantity=float(row['qt_indenizada']),
                reserve_quantity=float(row['qt_reservada']),
                pending_quantity=float(row['qt_pendente']),
                block_quantity=float(row['qt_bloqueada']),
                available_quantity=float(row['qt_disponivel']),
                sale_price=float(row['preco_venda']),
                last_stock_cost=float(row['custo_ult_entrada']),
                date_stock=row['data'],
                company=int(row['empresa']),
            )

            qs.save()
