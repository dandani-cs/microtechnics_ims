from django.db import models
from datetime import date
from django.utils.translation import gettext


class Projects(models.Model):
# Create your models here.
    class projectStatus(models.TextChoices):
        IN_PROGRESS = 'IP', _('In Progress')
        COMPLETE = 'C', _('Complete')

        def generate_uuid():
            return uuid.uuid4().hex[:10]


project_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
project_Name = models.CharField(max_length=20, null=False)
client_Name = models.CharField(max_length=32, null=False)
status = models.TextChoices()
date_Created = models.DateField(auto_now_add=True)