from core.models.products import Product


def writer_product(list_products, id_company):
    for product in list_products:

        qs_product = Product.objects.filter(
            code_product=product.code_product
        ).first()

        if not qs_product:
            qs = Product.objects.create(
                code_product=product.code_product,
                description_product=product.description_product,
                code_provider=product.code_provider,
                company=id_company,
                packaging=product.packaging,
                quantity_unit_box=product.quantity_unit_box,
                brand=product.brand,
                net_weight=product.net_weight ,
                active_principle=product.active_principle,
                code_factory=product.code_factory,
                code_ncm=product.ncm,
                code_auxiliary=product.code_auxiliary,
                code_department=product.code_department,
                code_section=product.code_section,
                description_department=product.description_department,
                description_section=product.description_section
            )

            qs.save()

        if qs_product:

            if qs_product.description_product != product.description_product or qs_product.code_provider != product.code_provider:
                qs_product.description_product = product.description_product
                qs_product.code_provider = product.code_provider
                qs_product.sent = False

                qs_product.save()
