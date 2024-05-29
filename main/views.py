from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from . import models
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def education(request):
    template = loader.get_template('education.html')
    data = {
        'courses' : [
            {'name' : 'Samskruthi eng. College','course' : 'B Tech (Data science) (2021-2025)','percentage' : '7.0',},
            {'name' : 'SriSandepani jr. college','course' : 'Intermediate (2019-2021)','percentage' : '6.5',},
            {'name' : 'Kanthi high school','course' : 'SSC (2009-2019)','percentage' : '9.8',},
        ]
    }
    return HttpResponse(template.render(data,request))

def learning(request):
    template = loader.get_template('learning.html')
    return HttpResponse(template.render())

def projects(request):
    template = loader.get_template('projects.html')
    project = models.project.objects.all()[::-1]
    print(project)
    data = {
        'projects' : project,
        }
    return HttpResponse(template.render(data,request))

def project(request,project_name):
    template = loader.get_template('project.html')
    project_details = models.project.objects.get(project_id=project_name)
    print(project_details)
    data = {'project' : project_details}
    return HttpResponse(template.render(data,request))

def resume(request):
    template = loader.get_template('resume.html')
    return HttpResponse(template.render())

def skills(request):
    template = loader.get_template('skills.html')
    data = {
        'skills' : ['git','python','docker'],
    }
    return HttpResponse(template.render(data,request))

def social(request):
    template = loader.get_template('social.html')
    social = models.social_links.objects.all()
    data = {
        'social' : social,
    }
    return HttpResponse(template.render(data,request))