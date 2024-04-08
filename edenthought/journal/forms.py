# Import user creation form from django
from django.contrib.auth.forms import UserCreationForm # Used to create a user
# Import login forms from django
from django.contrib.auth.forms import AuthenticationForm # Used to authenticate a user
from django import forms # Import forms from django
from django.forms.widgets import PasswordInput, TextInput # Import password and text input widgets from django


# Import the user model from django
from django.contrib.auth.models import User # Built-in user model from Django

# Import the model form class
from django.forms import ModelForm
# Import the Thought model
from . models import Thought     # Import the Thought model from the models file

# Create modelform class
class CreateUserForm(UserCreationForm):
    # Meta class
    class Meta:
        # Model to be used
        model = User
        # Require email to be entered
        model.email = True
        # Fields to be displayed
        fields = ['username', 'email', 'password1', 'password2'] # Password1 and password2 are the passwords to be entered by the user (password1 is the password and password2 is the confirmation password

# Create a login form class
class LoginForm(AuthenticationForm):
    # Meta class
    class Meta:
        # Fields to be displayed
        fields = ['username', 'password'] # Username and password fields to be displayed
        # Widgets to be used
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), # Username field widget
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), # Password field widget
        }
        
# Create a form for the journal entry
class ThoughtForm(ModelForm):
    # Meta class
    class Meta:
        # Model to be used
        model = Thought
        # Fields to be displayed
        fields = ['title', 'content'] # Title and content fields to be displayed
        # Widgets to be used
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}), # Title field widget
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}), # Content field widget
        }