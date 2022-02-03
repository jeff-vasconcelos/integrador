from core.models.orders import OrdersBuy


def writer_order(dataframe_orders):
    # iterando dataframe
    for index, row in dataframe_orders.iterrows():

        # buscando dados existentes
        qs_order = OrdersBuy.objects.filter(
            code_product=int(row['cod_produto']),
            code_branch=int(row['cod_filial']),
            code_provider=int(row['cod_fornecedor']),
            order_number=int(row['num_pedido'])
        ).first()

        #  atualizando dados existentes
        if qs_order:
            if qs_order.quantity_over != float(row['saldo']) or qs_order.date_order != row['data']:
                qs_order.quantity_over = float(row['saldo'])
                qs_order.date_order = row['data']
                qs_order.sent=False

                qs_order.save()

        # gravando novos dados
        else:
            qs = OrdersBuy.objects.create(
                code_product=int(row['cod_produto']),
                code_branch=int(row['cod_filial']),
                code_provider=int(row['cod_fornecedor']),
                company=int(row['empresa']),
                order_number=int(row['num_pedido']),
                quantity_over=float(row['saldo']),
                date_order=row['data']
            )

            qs.save()
