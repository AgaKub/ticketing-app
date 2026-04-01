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
    inlines = [OrderItemInline]

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(TicketType)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)


