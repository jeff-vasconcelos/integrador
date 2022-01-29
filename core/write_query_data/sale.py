from core.models.sales import SaleProduct


def writer_sale(list_sales, id_company):
    for sale in list_sales:

        qs_sale = SaleProduct.objects.filter(
            code_product=sale.code_product,
            code_branch=sale.code_product,
            code_provider=sale.code_provider,
            quantity_sales=sale.quantity_sales,
            price_unit=sale.price_unit,
            financial_cost=sale.financial_cost,
            date_sale=sale.date_sale
        ).first()

        if not qs_sale:
            qs = SaleProduct.objects.create(
                code_product=sale.code_product,
                code_branch=sale.code_product,
                code_provider=sale.code_provider,
                company=id_company,
                quantity_sales=sale.quantity_sales,
                price_unit=sale.price_unit,
                financial_cost=sale.financial_cost,
                client=sale.client,
                note_number=sale.note_number,
                rca=sale.rca,
                supervisor=sale.supervisor,
                date_sale=sale.date_sale
            )

            qs.save()
