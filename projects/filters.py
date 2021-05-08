import django_filters
from .models import Projects

class ProjectsFilter(django_filters.FilterSet):
    class Meta:
        model = Projects
        fields = '__all__'