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
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return f"{self.name} - {self.event.name}"
    