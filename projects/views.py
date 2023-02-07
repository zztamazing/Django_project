from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

from .utils import searchProjects


# Create your views here.


def projects(request):
    # return HttpResponse(f'<h1>Welcome to page1</h1>')


    projectList, search_query = searchProjects(request)

    context = {
        'projects': projectList,
        'search_query': search_query,
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


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        post_form = ProjectForm(request.POST, request.FILES)
        if post_form.is_valid():
            project = post_form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {
        'form': form,
    }
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
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


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {
        'object': profile,
    }
    return render(request, 'projects/delete_template.html', context)
