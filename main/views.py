from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


def education(request):
    template = loader.get_template('education.html')
    return HttpResponse(template.render())


def learning(request):
    template = loader.get_template('learning.html')
    return HttpResponse(template.render())


def projects(request):
    template = loader.get_template('projects.html')
    return HttpResponse(template.render())

def resume(request):
    template = loader.get_template('resume.html')
    return HttpResponse(template.render())

def skills(request):
    template = loader.get_template('skills.html')
    return HttpResponse(template.render())

def social(request):
    template = loader.get_template('social.html')
    return HttpResponse(template.render())