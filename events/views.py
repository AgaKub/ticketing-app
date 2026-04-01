import email

from django.shortcuts import render, redirect
from .models import Event, Order, TicketType, OrderItem



def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    tickets = event.ticket_types.all()

    general_admission_ticket = None
    for ticket in tickets:
        if ticket.name.lower() == "general admission":
            general_admission_ticket = ticket
            break
        
    print("GA ticket:", general_admission_ticket)

    ticket_data = []

    for ticket in tickets:
        save_percent = None

        if general_admission_ticket and ticket.price < general_admission_ticket.price:
            save_percent = round(
                ((general_admission_ticket.price - ticket.price) / general_admission_ticket.price) * 100
            )

        ticket_data.append({
            'ticket': ticket,
            'save_percent': save_percent
        })

    return render(request, 'events/event_detail.html', {
        'event': event,
        'ticket_data': ticket_data
    })



def checkout(request):
    selections = []

    for ticket_name, qty in request.GET.items():
        if qty.isdigit() and int(qty) > 0:
            selections.append({
                'ticket': ticket_name,
                'qty': qty
            })

    if not selections:
        return redirect('/')

    return render(request, 'events/checkout.html', {
        'selections': selections
    })



def email_step(request):
    selections = []

    for ticket_name, qty in request.GET.items():
        if qty.isdigit() and int(qty) > 0:
            selections.append({
                'ticket': ticket_name,
                'qty': qty
            })

    if not selections:
        return redirect('/')

    return render(request, 'events/email.html', {
        'selections': selections
    })



def payment_step(request):
    selections = []
    email = request.GET.get('email')
    total = 0
    selected_tickets = []

    for key, value in request.GET.items():
        if key == 'email':
            continue

        if value.isdigit() and int(value) > 0:
            try:
                ticket = TicketType.objects.get(name=key)
                qty = int(value)
                subtotal = ticket.price * qty
                total += subtotal

                selections.append({
                    'ticket': ticket.name,
                    'qty': qty,
                    'price': ticket.price,
                    'subtotal': subtotal
                })

                selected_tickets.append({
                    'ticket_obj': ticket,
                    'qty': qty
                })

            except TicketType.DoesNotExist:
                continue

    if not selections or not email:
        return redirect('/')

    event = selected_tickets[0]['ticket_obj'].event

    for item in selected_tickets:
        if item['ticket_obj'].event != event:
            return redirect('/')

    order = Order.objects.create(
        event=event,
        email=email,
        total=total
    )

    for item in selected_tickets:
        OrderItem.objects.create(
            order=order,
            ticket_type=item['ticket_obj'],
            quantity=item['qty']
        )

    return render(request, 'events/payment.html', {
        'selections': selections,
        'email': email,
        'total': total,
        'order': order
    })




def privacy_policy(request):
    return render(request, 'events/privacy_policy.html')

