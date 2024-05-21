from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('education/',views.education,name="education"),
    path('learning/',views.learning,name="learning"),
    path('projects/',views.projects,name="projects"),
    path('resume/',views.resume,name="resume"),
    path('skills/',views.skills,name="skills"),
    path('social/',views.social,name="resume"),
    
    #
]
