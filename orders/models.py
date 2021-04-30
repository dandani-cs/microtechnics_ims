from django.db import models
import uuid

from accounts.models import User

def generate_uuid():
    return uuid.uuid4().hex[:10].upper()

class Order(models.Model):
    order_num = models.CharField(max_length  = 10,
                                 primary_key = True,
                                 unique      = True,
                                 default     = generate_uuid)
    # TODO: change this once Project model has been created
    project_id     = models.CharField(max_length = 10, default = generate_uuid)
    items          = models.JSONField(null = False)
    total_price    = models.DecimalField(max_digits = 16, decimal_places = 2)
    is_approved    = models.BooleanField(default = False)
    date_created   = models.DateTimeField(auto_now_add = True)
    requested_user = models.ForeignKey(User,
                                       on_delete    = models.SET_NULL,
                                       null         = True,
                                       related_name = "order_requested_by")
    approved_admin = models.ForeignKey(User,
                                       on_delete    = models.SET_NULL,
                                       null         = True,
                                       related_name = "order_approved_by")
