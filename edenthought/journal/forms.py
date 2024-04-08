# Import user creation form from django
from django.contrib.auth.forms import UserCreationForm # Used to create a user

# Import the user model from django
from django.contrib.auth.models import User # Built-in user model from Django

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

