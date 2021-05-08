from django.forms import ModelForm
from .models import Projects

class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = ('projects_Name', 'clients_Name', 'status')   

