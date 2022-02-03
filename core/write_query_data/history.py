from core.models.histories import HistoryProduct


def writer_history(dataframe_histories):
    # iterando dataframe
    for index, row in dataframe_histories.iterrows():

        # buscando dados existentes
        qs_history = HistoryProduct.objects.filter(
            code_product=int(row['cod_produto']),
            code_branch=int(row['cod_filial']),
            code_provider=int(row['cod_fornecedor']),
        ).first()

        #  atualizando dados existentes
        if qs_history:
            if qs_history.quantity_stock != float(row['qt_estoque']) or qs_history.date_stock != row['data']:
                qs_history.quantity_stock = float(row['qt_estoque'])
                qs_history.date_stock = (row['data'])
                qs_history.sent=False

                qs_history.save()

        # gravando novos dados
        else:
            qs = HistoryProduct.objects.create(
                code_product=int(row['cod_produto']),
                code_branch=int(row['cod_filial']),
                code_provider=int(row['cod_fornecedor']),
                company=int(row['empresa']),
                quantity_stock=float(row['qt_estoque']),
                date_stock=row['data']
            )

            qs.save()
