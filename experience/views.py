from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ContactForm

# Create your views here.

def home(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "main.html", {'form':form})

# def contact_view(request):
#     form = ContactForm()

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_success')
#         # else:
#         #     form = ContactForm()
#     return render(request, 'contact.html', {'form':form})
    
# def contact_success(request):
#     return render(request, 'success.html')