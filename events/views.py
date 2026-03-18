from django.shortcuts import render
from .models import Event, TicketType


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    tickets = event.ticket_types.all()
    return render(request, 'events/event_detail.html', {
        'event': event,
        'tickets': tickets
    })


# Create your views here.
