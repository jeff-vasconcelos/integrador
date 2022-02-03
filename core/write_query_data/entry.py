from core.models.entries import EntryProduct


def writer_entry(dataframe_entries):
    # iterando dataframe
    for index, row in dataframe_entries.iterrows():

        qs_entry = EntryProduct.objects.filter(
            code_product=int(row['cod_produto']),
            code_branch=int(row['cod_filial']),
            code_provider=int(row['cod_fornecedor'])
        ).first()

        #  atualizando dados existentes
        if qs_entry:
            if qs_entry.quantity_last_entry != float(row['qt_ult_entrada']) or qs_entry.date_last_entry != float(row['vl_ult_entrada']):
                qs_entry.quantity_last_entry = float(row['qt_ult_entrada'])
                qs_entry.value_last_entry = float(row['vl_ult_entrada'])
                qs_entry.date_last_entry = row['data']
                qs_entry.sent = False

                qs_entry.save()

        # gravando novos dados
        else:
            qs = EntryProduct.objects.create(
                code_product=int(row['cod_produto']),
                code_branch=int(row['cod_filial']),
                code_provider=int(row['cod_fornecedor']),
                company=int(row['empresa']),
                quantity_last_entry=float(row['qt_ult_entrada']),
                value_last_entry=float(row['qt_ult_entrada']),
                date_last_entry=row['data']
            )

            qs.save()
