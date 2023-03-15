from django.contrib import admin

from warehouses.models import Warehouse, WarehouseDetail, WarehouseItem

admin.site.register(Warehouse)

admin.site.register(WarehouseDetail)

admin.site.register(WarehouseItem)
