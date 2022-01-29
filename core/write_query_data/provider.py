from core.models.providers import Provider


def writer_provider(list_providers, id_company):
    for provider in list_providers:

        qs_provider = Provider.objects.filter(
            code_provider=provider.code_provider
        ).first()

        if not qs_provider:
            qs = Provider.objects.create(
                code_provider=provider.code_provider,
                description_provider=provider.description_provider,
                cnpj=provider.cnpj,
                state_registration=provider.state_registration,
                company=id_company
            )

            qs.save()

        if qs_provider:

            if qs_provider.description_provider != provider.description_provider or qs_provider.cnpj != provider.cnpj:
                qs_provider.description_provider = provider.description_provider
                qs_provider.cnpj = provider.cnpj
                qs_provider.sent=False

                qs_provider.save()
