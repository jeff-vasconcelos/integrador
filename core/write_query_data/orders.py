from core.models.orders import OrdersBuy


def writer_order(list_histories, id_company):
    for order in list_histories:

        qs_order = OrdersBuy.objects.filter(
            code_product=order.code_product,
            code_branch=order.code_product,
            code_provider=order.code_provider,
            order_number=order.order_number
        ).first()

        if qs_order:
            if qs_order.quantity_over != order.quantity_over or qs_order.date_order != order.date_order:
                qs_order.quantity_over = order.quantity_over
                qs_order.date_order = order.date_order
                qs_order.sent=False

                qs_order.save()

        else:
            qs = OrdersBuy.objects.create(
                code_product=order.code_product,
                code_branch=order.code_product,
                code_provider=order.code_provider,
                company=id_company,
                order_number=order.order_number,
                quantity_over=order.quantity_over,
                date_order=order.date_order
            )

            qs.save()
