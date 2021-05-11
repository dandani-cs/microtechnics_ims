from django.db import models
from inventory.models import Item

# Create your models here.
class Notification(models.Model):
    LOW = 'low'
    CRITICAL = 'critical'
    OUT_OF_STOCK = 'out of stock'

    CHOICES = {
        (LOW, 'Message'), 
        (CRITICAL, 'Critical'),
        (OUT_OF_STOCK, 'Out of Stock')
    }

    # reference to Item model
    to_inv = models.ForeignKey(Item, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']