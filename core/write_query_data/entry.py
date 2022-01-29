from core.models.entries import EntryProduct


def writer_entry(list_entries, id_company):
    for entry in list_entries:

        qs_entry = EntryProduct.objects.filter(
            code_product=entry.code_product,
            code_branch=entry.code_product,
            code_provider=entry.code_provider
        ).first()

        if qs_entry:
            if qs_entry.quantity_last_entry != entry.quantity_last_entry or qs_entry.date_last_entry != entry.date_last_entry:
                qs_entry.quantity_last_entry = entry.quantity_last_entry
                qs_entry.value_last_entry = entry.value_last_entry
                qs_entry.date_last_entry = entry.date_last_entry
                qs_entry.sent = False

                qs_entry.save()

        else:
            qs = EntryProduct.objects.create(
                code_product=entry.code_product,
                code_branch=entry.code_product,
                code_provider=entry.code_provider,
                company=id_company,
                quantity_last_entry=entry.quantity_last_entry,
                value_last_entry=entry.value_last_entry,
                date_last_entry=entry.date_last_entry
            )

            qs.save()
