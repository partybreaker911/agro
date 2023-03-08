from django.contrib import admin

from catalogs.models import ProductCategory, Product, State, Region, Location


class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = (
        "name",
        "parent",
    )


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = (
        "category",
        "name",
    )


admin.site.register(Product, ProductAdmin)


class StateAdmin(admin.ModelAdmin):
    model = State
    list_display = [
        "name",
    ]


admin.site.register(State, StateAdmin)


class RegionAdmin(admin.ModelAdmin):
    model = Region
    list_display = [
        "name",
        "state",
    ]


admin.site.register(Region, RegionAdmin)


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = [
        "name",
        "region",
    ]


admin.site.register(Location, LocationAdmin)
