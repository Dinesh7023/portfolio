from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ContactForm
from django.contrib import messages


# Create your views here.

def home(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent Successfully!")
            return redirect('/')
    else:
        form = ContactForm()
        
    return render(request, "main.html", {'form':form})

