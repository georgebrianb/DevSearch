from django.shortcuts import render, redirect
from django.http import HttpResponse
from operator import itemgetter
from .models import Project
from .forms import ProjectForm



# all projects view
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

# single project view
def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})


def createProject(request):
    # instantiate the form
    form = ProjectForm()
    
    # if method is POST, create the new project
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        # Django checks if everything is alright
        if form.is_valid():
            # saves the project
            form.save()
            
            # with the 'redirect' import we can redirect the user to the 
            # projects page. 
            # We are using the name that's been set in the urls.py file
            return redirect('projects')
    # pass the form as an attribute to the context object so we can render all of its fields            
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)



def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    # instantiate the form using the project identified by the pk that's been supplied via the URL
    form = ProjectForm(instance=project)
    
    # if method is POST, create the new project
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # Django checks if everything is alright
        if form.is_valid():
            # saves the project
            form.save()
            
            # with the 'redirect' import we can redirect the user to the 
            # projects page. 
            # We are using the name that's been set in the urls.py file
            return redirect('projects')
    # pass the form as an attribute to the context object so we can render all of its fields            
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    
    
    if request.method == 'POST':
        print(request.POST)
        project.delete()
        return redirect('projects')
    
    context = {'object': project.title}
    return render(request, 'projects/delete_template.html', context)
    
    


    