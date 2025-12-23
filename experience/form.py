from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Your Email Address'}),
            'message':forms.TextInput(attrs={'placeholder': 'Your Message'})
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")
        return name

