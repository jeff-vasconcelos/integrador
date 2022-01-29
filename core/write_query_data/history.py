from core.models.histories import HistoryProduct


def writer_history(list_histories, id_company):
    for history in list_histories:

        qs_history = HistoryProduct.objects.filter(
            code_product=history.code_product,
            code_branch=history.code_product,
            code_provider=history.code_provider,
        ).first()

        if qs_history:
            if qs_history.quantity_stock != history.quantity_stock or qs_history.date_stock != history.date_stock:
                qs_history.quantity_stock = history.quantity_stock
                qs_history.date_stock = history.date_stock
                qs_history.sent=False

                qs_history.save()

        else:
            qs = HistoryProduct.objects.create(
                code_product=history.code_product,
                code_branch=history.code_product,
                code_provider=history.code_provider,
                company=id_company,
                quantity_stock=history.quantity_stock,
                date_stock=history.date_stock
            )

            qs.save()
