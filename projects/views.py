from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.forms import ModelForm
from .models import Projects
from .forms import ProjectsForm
from .filters import ProjectsFilter 

class ProjectsView(ListView):
    model = Projects
    template_name = "projects.html"
    paginate_by = 10
    


def Add_Projects (request):
    projectsForm = ProjectsForm()
    contextForm = {'projectsForm': projectsForm}

    if request.method == 'POST':
       projectsForm = ProjectsForm(request.POST)
       if projectsForm.is_valid():
           projectsForm.save()
           return redirect('projects_view')
           
    return render(request, 'projects_add.html', contextForm)
    
  
def Edit_Projects (request, pk): 

    editProjects = Projects.objects.get(project_ID=pk)
    editForm = ProjectsForm(instance=editProjects)

    if request.method == 'POST':
       editForm = ProjectsForm(request.POST, instance=editProjects)
       if editForm.is_valid():
           editForm.save()
           return redirect('projects_view')

    contextEdit = {'editForm': editForm}
    return render(request, 'projects_edit.html', contextEdit)   




def Delete_Projects (request, pk):
    deleteProjects = Projects.objects.get(project_ID=pk)
    if request.method == 'POST':
       deleteProjects.delete()
       return redirect('projects_view')

    contextDelete = {'projectsDelete': deleteProjects}
    return render(request, 'projects_delete.html', contextDelete) 
    



