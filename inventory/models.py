from django.db import models
import uuid

# Create your models here.
def generate_uuid():
    return uuid.uuid4().hex[:10]

class CategoryOptions():
    CATEGORY_USER_ADDED = 0
    CATEGORY_HARD_CODED = 1
    CATEGORY_GENERAL    = 2

    CATEGORY_CHOICES = (
        (CATEGORY_USER_ADDED, 'User-added'),
        (CATEGORY_HARD_CODED, 'Hardcoded'),
        (CATEGORY_GENERAL,    'General'),
    )

class Category(models.Model):
    cat_id = models.CharField(max_length = 10, primary_key = True, unique = True, default = generate_uuid)
    name   = models.CharField(max_length = 20)
    option = models.IntegerField(choices = CategoryOptions.CATEGORY_CHOICES, default = 2)

class Item(models.Model):
    item_code    = models.CharField(max_length = 10, primary_key = True, unique = True, default = generate_uuid)
    name         = models.CharField(max_length = 20)
    price        = models.DecimalField(max_digits = 16, decimal_places = 2)
    quantity     = models.IntegerField(default = 0)
    category     = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    max_quantity = models.IntegerField(default = 0)
    description  = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
    def calc_quantity_level(item):
        thresholds = [ 0.1, 0.25, 1.0 ]
        percent    = item.quantity / item.max_quantity

        for t in range(len(thresholds)):
            if percent < thresholds[t]: return t
