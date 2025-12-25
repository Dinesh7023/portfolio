from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .form import ContactForm
from django.contrib import messages
from .models import *


# Create your views here.

def home(request):
    form = ContactForm()
    project = Project.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent Successfully!")
            return redirect('/')
    else:
        form = ContactForm()

    context = {
        'form':form,
        'project' : project
    }
        
    return render(request, "index.html", context)

def project_details(request, id):
    project = get_object_or_404(Project, id=id)

    context = {
        'project' : project
    }

    return render(request, "project_details.html", context)

