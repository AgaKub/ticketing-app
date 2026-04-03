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



admin.site.register(Event, EventAdmin)
admin.site.register(TicketType)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)