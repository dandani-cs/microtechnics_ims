from .views import ProjectsView
from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('projects_view', views.ProjectsView.as_view(), name="projects_view"),
    path('projects_add', views.Add_Projects, name="projects_add"),
    path('projects_edit/<str:pk>/', views.Edit_Projects, name="projects_edit"),
    path('projects_delete/<str:pk>/', views.Delete_Projects, name="projects_delete"),
] 