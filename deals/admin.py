from django.contrib import admin

from deals.models import Deal, ProductPrice


class DealAdmin(admin.ModelAdmin):
    model = Deal
    list_display = [
        "user",
        "product",
        "quantity",
        "total_price",
        "approved",
        "timestamp",
    ]


admin.site.register(Deal, DealAdmin)


class ProductPriceAdmin(admin.ModelAdmin):
    model = ProductPrice
    list_display = [
        "location",
        "product",
        "price",
        "works_until",
        "timestamp",
    ]


admin.site.register(ProductPrice, ProductPriceAdmin)
