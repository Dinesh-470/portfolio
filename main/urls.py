from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('education/',views.education,name="education"),
    path('learning/',views.learning,name="learning"),
    path('resume/',views.resume,name="resume"),
    path('skills/',views.skills,name="skills"),
    path('social/',views.social,name="resume"),
    
    #projects and project-details
    path('projects/',views.projects,name="projects"),
    path('projects/<str:project_name>',views.project),
    
    #404
    path('404/',views.notfound,name='404'),
    
    #api
    path('u/api/projects',views.projects_api),
    path('u/api/skills',views.skills_api),
    path('u/api/education',views.education_api),
]
