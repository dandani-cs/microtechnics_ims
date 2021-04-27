from django.urls import path
from . import views


# Create your views here.
urlpatterns = [
    path('projects', views.projects, name="projects_view")
] 