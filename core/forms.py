from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ContactSubmission, RatingRequest, RatingRequestMessage


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']


class RatingRequestForm(forms.ModelForm):
    class Meta:
        model = RatingRequest
        fields = ['company_name', 'description']


class RatingRequestMessageForm(forms.ModelForm):
    class Meta:
        model = RatingRequestMessage
        fields = ['message']
