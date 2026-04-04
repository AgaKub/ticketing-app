import email

from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Event, TicketType, Order, OrderItem


def event_list(request):
    release_expired_orders()
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})



def event_detail(request, event_id):
    release_expired_orders()
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



def release_expired_orders():
    print("CLEANER RAN")
    
    expired_orders = Order.objects.filter(
        status='pending',
        expires_at__isnull=False,
        expires_at__lt=timezone.now()
    )

    print("EXPIRED ORDERS FOUND:", expired_orders.count())
    
    for order in expired_orders:
        items = OrderItem.objects.filter(order=order)

        for item in items:
            ticket = item.ticket_type
            ticket.quantity += item.quantity
            ticket.save()

        order.status = 'expired'
        order.save()
        


def payment_step(request):
    release_expired_orders()

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

                # backend safety limit
                if qty > 10 or qty > ticket.quantity:
                    return redirect('/')

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

    # check all tickets belong to the same event
    for item in selected_tickets:
        if item['ticket_obj'].event != event:
            return redirect('/')

    # create order
    order = Order.objects.create(
        event=event,
        email=email,
        total=total,
        status='pending',
        expires_at=timezone.now() + timedelta(minutes=10)
    )

    # create order items + reduce stock
    for item in selected_tickets:
        ticket = item['ticket_obj']
        qty = item['qty']

        if ticket.quantity >= qty:
            ticket.quantity = ticket.quantity - qty
            ticket.save()

            OrderItem.objects.create(
                order=order,
                ticket_type=ticket,
                quantity=qty
            )
        else:
            return redirect('/')

    return render(request, 'events/payment.html', {
        'selections': selections,
        'email': email,
        'total': total,
        'order': order
    })


def privacy_policy(request):
    return render(request, 'events/privacy_policy.html')

