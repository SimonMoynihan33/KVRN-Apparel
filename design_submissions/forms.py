from django import forms
from .models import UserDesignSubmission


class UserDesignSubmissionForm(forms.ModelForm):
    """
    Form to allow users to submit a design to be used in
    our shop.
    """
    class Meta:
        model = UserDesignSubmission
        fields = ['title', 'description', 'image', 'email']
