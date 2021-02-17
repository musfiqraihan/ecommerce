from django.contrib import admin
from .models import ItemList, OrderItemList, OrderList, CategoryList


admin.site.register(CategoryList)
admin.site.register(ItemList)
admin.site.register(OrderItemList)
admin.site.register(OrderList)

