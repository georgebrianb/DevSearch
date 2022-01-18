from django.shortcuts import render
from django.http import HttpResponse
from operator import itemgetter

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    page = "projects"
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for project in projectsList:
        if project['id'] == pk:
            projectObj = project
            return render(request, 'projects/single-project.html', {'project': projectObj})
        else:
            continue
    return render(request, 'projects/single-project.html', {'project': {'title':f'There is no project with the id of {pk}'}})
    
