from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Contact form for user to contact site Admins """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
