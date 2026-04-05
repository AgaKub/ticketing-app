from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    date = models.DateTimeField()
    capacity = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return self.name


class TicketType(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_types')
    total_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.available_quantity is None:
            self.available_quantity = self.total_quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.event.name}"



ORDER_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('paid', 'Paid'),
    ('expired', 'Expired')
]


class Order(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    total = models.DecimalField(max_digits=8, decimal_places=2)

    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    expires_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.email}"
    

 

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.ticket_type.name} x {self.quantity}"
    
