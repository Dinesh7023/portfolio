from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Your Email Address'}),
            'message':forms.TextInput(attrs={'placeholder': 'Your Message'},)
        }
