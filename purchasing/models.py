from django.db import models
import uuid

from accounts.models import User

# Create your models here.
def generate_uuid():
    return uuid.uuid4().hex[:10].upper()


class StatusPurchasingOptions():
    STATUS_CANCELLED = 0
    STATUS_FOR_APPROVAL = 1
    STATUS_APPROVED = 2
    STATUS_RECEIVED = 3

    STATUS_CHOICES = (
                      (STATUS_CANCELLED, 'Cancelled'),
                      (STATUS_FOR_APPROVAL, 'For Approval'),
                      (STATUS_APPROVED, 'Approved'),
                      (STATUS_RECEIVED, 'Received'),
    )


class Purchasing(models.Model):
    purchase_num = models.CharField(max_length = 10,
                                    primary_key = True,
                                    unique = True,
                                    default = generate_uuid)
    items = models.JSONField(null = False)
    total_price = models.DecimalField(max_digits = 16,
                                      decimal_places = 2)
    requested_user = models.ForeignKey(User,
                                       on_delete = models.SET_NULL,
                                       null = True,
                                       related_name = "requested_by")
    approved_admin = models.ForeignKey(User,
                                       on_delete = models.SET_NULL,
                                       null = True,
                                       related_name = "approved_by")
    status = models.IntegerField(choices = StatusPurchasingOptions.STATUS_CHOICES, default = 1)
    date_created = models.DateTimeField(auto_now_add=True)
