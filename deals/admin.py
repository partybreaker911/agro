from django.contrib import admin

from deals.models import Deal, ProductPrice

admin.site.register(Deal)


class ProductPriceAdmin(admin.ModelAdmin):
    model = ProductPrice
    list_display = ["location", "product", "price", "works_until", "timestamp"]


admin.site.register(ProductPrice, ProductPriceAdmin)
