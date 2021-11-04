from django import forms
from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.forms.fields import CharField
from django.forms.widgets import PasswordInput, Widget

# using django sign-up auto feature
# used to create institutions


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']


# Students signin form. noot working as at now
class attendeeUserForm(ModelForm):
    class Meta:
        model = institutionExtra_ID
        fields = '__all__'

# forms created from models for use in detail addition

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'


class ActivityForm(ModelForm):
    class Meta:
        model = Activitie
        fields = '__all__'
        labels = {
            'session_name': '',
            'venue': 'Venue',
            'session_date': '',
            'session_time': '',
            'session_duration': '',
        }
        widgets = {
            'session_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of activity'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'session_date': forms.DateInput(attrs={'class': 'form-date', 'type': 'dateinput', 'placeholder': 'Date of activity'}),
            'session_time': forms.TimeInput(attrs={'class': 'form-time', 'placeholder': 'Time...'}),
            'session_duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Duration'}),
        }


class attendeeForm(ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        labels = {
            'institutionID': '',
            'attendee_name': '',
            'attendee_mail': '',
            'attendee_ID': ''
        }
        widgets = {
            'institutionID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institution Register Key'}),
            'attendee_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My name is...'}),
            'attendee_mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'attendee@gmail.com'}),
            'attendee_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Membership ID'})
        }

