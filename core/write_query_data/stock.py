from core.models.stock import StockProduct


def writer_stock(list_stock, id_company):
    for stock in list_stock:

        qs_stock = StockProduct.objects.filter(
            code_product=stock.code_product,
            code_branch=stock.code_product,
            code_provider=stock.code_provider
        ).first()

        if qs_stock:

            qs_stock.general_quantity = stock.general_quantity,
            qs_stock.indemnify_quantity = stock.indemnify_quantity,
            qs_stock.reserve_quantity = stock.reserve_quantity,
            qs_stock.pending_quantity = stock.pending_quantity,
            qs_stock.block_quantity = stock.block_quantity,
            qs_stock.available_quantity = stock.available_quantity,
            qs_stock.sale_price = stock.sale_price,
            qs_stock.last_stock_cost = stock.last_stock_cost,
            qs_stock.date_stock = stock.date_stock,
            qs_stock.sent = False

            qs_stock.save()

        else:
            qs = StockProduct.objects.create(
                code_product=stock.code_product,
                code_branch=stock.code_product,
                code_provider=stock.code_provider,
                general_quantity = stock.general_quantity,
                indemnify_quantity = stock.indemnify_quantity,
                reserve_quantity = stock.reserve_quantity,
                pending_quantity = stock.pending_quantity,
                block_quantity = stock.block_quantity,
                available_quantity = stock.available_quantity,
                sale_price = stock.sale_price,
                last_stock_cost = stock.last_stock_cost,
                date_stock = stock.date_stock,
                company=id_company,
            )

            qs.save()
