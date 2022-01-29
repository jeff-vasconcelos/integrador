from django.contrib import admin
from core.models.configuration import Configuration
from core.models.providers import Provider
from core.models.products import Product
from core.models.sales import SaleProduct
from core.models.histories import HistoryProduct
from core.models.orders import OrdersBuy
from core.models.entries import EntryProduct
from core.models.stock import StockProduct

admin.site.register(Configuration)
admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(SaleProduct)
admin.site.register(HistoryProduct)
admin.site.register(OrdersBuy)
admin.site.register(EntryProduct)
admin.site.register(StockProduct)
