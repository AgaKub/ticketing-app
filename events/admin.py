from django.contrib import admin
from .models import Event, TicketType, Order, OrderItem


class TicketTypeInline(admin.TabularInline):
    model = TicketType
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [TicketTypeInline]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'event',
        'email',
        'total',
        'status',
        'expires_at',
        'created_at'
    )
    list_display_links = ('id', 'event', 'email')
    list_filter = ('status', 'event')
    search_fields = ('email',)
    inlines = [OrderItemInline]


class TicketTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event',
        'price',
        'total_quantity',
        'available_quantity',
        'sold_quantity',
        'is_active'
    )

    def sold_quantity(self, obj):
        return obj.total_quantity - obj.available_quantity

    sold_quantity.short_description = 'Sold'

    


admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
