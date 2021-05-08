from django.db import models
from datetime import date
from django.utils.translation import gettext
import uuid

def generate_uuid_projects():
    return uuid.uuid4().hex[:6]

class ProjectStatus():
    WORK_IN_PROGRESS_STATUS = 'WIP'
    COMPLETED_STATUS        = 'C'
    
    STATUS_CHOICES = (
        ('', '--Please Choose A Status--'),
        (WORK_IN_PROGRESS_STATUS, 'Work In Progress'),
        (COMPLETED_STATUS, 'Completed'),
    )



class Projects(models.Model):
    # Create your models here.
    project_ID      = models.CharField(max_length=6, primary_key=True, unique=True, default=generate_uuid_projects)
    projects_Name   = models.CharField(max_length=20, null=False)
    clients_Name    = models.CharField(max_length=32, null=False)
    status          = models.CharField(max_length=3, choices = ProjectStatus.STATUS_CHOICES, default = '')
    date_Created    = models.DateField(auto_now_add=True)

    


