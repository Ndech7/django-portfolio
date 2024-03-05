from django.shortcuts import render
from .models import Project


# Create your views here.
# a view to show a snippet of information about each project
def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/project_index.html", context)


# a view to display more info about each project
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "projects/project_detail.html", context)
