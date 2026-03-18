from django.contrib import admin
from .models import Event, TicketType 


class TicketTypeInline(admin.TabularInline):
    model = TicketType
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [TicketTypeInline]


# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(TicketType)
