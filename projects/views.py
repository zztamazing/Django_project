from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.
from django.http import HttpResponse


def projects(request):
    # return HttpResponse(f'Welcome to page1')
    projectList = Project.objects.all()
    page = 'projects'
    number = 1

    context = {
        'page': page,
        'number': number,
        'projects': projectList,

    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()

    context = {
        'tags': tags,
        'project': projectObj,
    }
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        post_form = ProjectForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('projects')

    context = {
        'form': form,
    }
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        post_form = ProjectForm(request.POST, request.FILES, instance=project)
        if post_form.is_valid():
            post_form.save()
            return redirect('projects')

    context = {
        'form': form,
    }
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    object = Project.objects.get(id=pk)

    if request.method == "POST":
        object.delete()
        return redirect('projects')
    context = {
        'object': object,
    }
    return render(request, 'projects/delete_template.html', context)
