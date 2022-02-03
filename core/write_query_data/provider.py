from core.models.providers import Provider


def writer_provider(dataframe_providers):
    # iterando dataframe
    for index, row in dataframe_providers.iterrows():

        # buscando dados existentes
        qs_provider = Provider.objects.filter(code_provider=str(row['cod_fornecedor'])).first()

        # gravando novos dados
        if not qs_provider:
            print("salvou: ", int(row['cod_fornecedor']))

            qs = Provider.objects.create(
                code_provider=int(row['cod_fornecedor']),
                description_provider=str(row['desc_fornecedor']),
                cnpj=str(row['cnpj']),
                state_registration=str(row['iestadual']),
                company=int(row['empresa'])
            )

            qs.save()

        #  atualizando dados existentes
        if qs_provider:

            if qs_provider.description_provider != str(row['desc_fornecedor']) or qs_provider.cnpj != str(row['cnpj']):
                print("atualizou: ", int(row['cod_fornecedor']))

                qs_provider.description_provider = str(row['desc_fornecedor'])
                qs_provider.cnpj = str(row['cnpj'])
                qs_provider.sent = False

                qs_provider.save()
