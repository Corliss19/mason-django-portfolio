from django.shortcuts import render
from projects.models import Project

# Create your views here.
def home_page(request):
    #projects = Project.objects.all()
    return render(request, 'homepage/homepage.html')

# might need {'projects': projects} dictionary