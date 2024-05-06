from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Client, Product, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'reg_date', 'client', 'total_price']
    ordering = ['-reg_date', 'total_price']
    list_filter = ['reg_date', 'total_price']
    readonly_fields = ['reg_date']

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['description', 'name']
    search_help_text = 'Поиск по названию или описанию продукта.'
    readonly_fields = ['reg_date', 'image', 'picture']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'О товаре',
            {
                'classes': ['collapse'],
                'description': 'Собственно о товаре',
                'fields': ['description', 'price'],
            },
        ),
        (
            'На складе',
            {
                'classes': ['collapse'],
                'description': 'Что на складе по товару',
                'fields': ['quantity'],
            },
        ),
    ]


admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
