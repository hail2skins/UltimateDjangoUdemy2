from django.shortcuts import render
from django.shortcuts import redirect # Import redirect function from django

# Import forms model class for user creation
from .forms import CreateUserForm, LoginForm, ThoughtForm, ProfileManagementForm, ProfilePicForm

# Import login modules from django
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Import decorator for login required
from django.contrib.auth.decorators import login_required

# Import module for flash messages
from django.contrib import messages

# Import the Thought model
from .models import Thought, Profile

# Import the User model from Django 
from django.contrib.auth.models import User


# Create your views here.
# Create a view for the home page
def home(request):
    
    # Render the home page template
    return render(request, 'journal/index.html')

# User registration view
def register(request):
    # Create an instance of the CreateUserForm class
    form = CreateUserForm()
    
    # Check if the form has been submitted
    if request.method == 'POST':
        # Create an instance of the CreateUserForm class with the data from the form
        form = CreateUserForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Variable to store user to create profile associated with the user
            current_user = form.save(commit=False)
            # Save the form
            form.save()
            # Create a profile for the user
            profile = Profile.objects.create(user=current_user)
            # Add message for success
            messages.success(request, 'Account created successfully!')
            # Redirect to the login page
            return redirect('login')
            
    # Create a dictionary to store the form
    context = {
        'form': form,
    }
    
    # Render the registration page template
    return render(request, 'journal/register.html', context)

# Login view
def login(request):
    # Create a new instance of the LoginForm model
    form = LoginForm()
    
    # Check if the form has been submitted using if statement
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Get the username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            
            # Check if user exists
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard') # Redirect to the dashboard view
    
    context = {
        'form': form,
    }
    
    
    return render(request, 'journal/login.html', context) # Add this function to render the login.html template

# Logout view
def logout(request):
    auth.logout(request)
    return redirect('')

# User profile/dashboard view
@login_required(login_url='login') # Add this decorator to the dashboard view preventing unauthorized access
def dashboard(request):
    
    # Get profile picture for user
    profile_pic = Profile.objects.get(user=request.user)
    
    # Create a dictionary to store the profile picture
    context = {
        'profile_pic': profile_pic,
    }
    
    # Render the dashboard page template
    return render(request, 'journal/dashboard.html', context)

# Create a view for the journal entry
@login_required(login_url='login') # Add this decorator to the create_thought view preventing unauthorized access
def create_thought(request):
    # Create an instance of the ThoughtForm class
    form = ThoughtForm()
    
    # Check if the form has been submitted
    if request.method == 'POST':
        # Create an instance of the ThoughtForm class with the data from the form
        form = ThoughtForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Variable to store the form
            thought = form.save(commit=False)
            # Set the user to the current user
            thought.user = request.user
            # Save the form
            thought.save()
            # Add message for success
            messages.success(request, 'Journal entry created successfully!')
            # Redirect to the dashboard page
            return redirect('my-thoughts')
            
    # Create a dictionary to store the form
    context = {
        'form': form,
    }
    
    # Render the create thought page template
    return render(request, 'journal/create_thought.html', context)

# Create a view for the user thoughts
@login_required(login_url='login') # Add this decorator to the my_thoughts view preventing unauthorized access
def my_thoughts(request):
    # Retrieve the current user id
    current_user = request.user.id
    
    # Get all the thoughts for the current user
    thoughts = Thought.objects.filter(user=current_user)
    
    # Create a dictionary to store the thoughts
    context = {
        'thoughts': thoughts,
    }
    
    # Render the my thoughts page template
    return render(request, 'journal/my-thoughts.html', context)

# Create a view to update a user thought
@login_required(login_url='login') # Add this decorator to the update_thought view preventing unauthorized access
def update_thought(request, pk):
    # generate a try and except block to handle the error
    try:
        # Get the thought by the primary key, and the current user
        thought = Thought.objects.get(id=pk, user=request.user)
    except:
        messages.error(request, 'Journal entry not found!')
        return redirect('my-thoughts')
    
    # Create an instance of the ThoughtForm class
    form = ThoughtForm(instance=thought)
    
    # Check if the form has been submitted
    if request.method == 'POST':
        # Create an instance of the ThoughtForm class with the data from the form
        form = ThoughtForm(request.POST, instance=thought)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form
            form.save()
            # Add message for success
            messages.success(request, 'Journal entry updated successfully!')
            # Redirect to the my thoughts page
            return redirect('my-thoughts')
            
    # Create a dictionary to store the form
    context = {
        'form': form,
    }
    
    # Render the update thought page template
    return render(request, 'journal/update_thought.html', context)

# Create a view to delete a user thought
@login_required(login_url='login') # Add this decorator to the delete_thought view preventing unauthorized access
def delete_thought(request, pk):
    # generate a try and except block to handle the error
    try:
        # Get the thought by the primary key, and the current user
        thought = Thought.objects.get(id=pk, user=request.user)
    except:
        messages.error(request, 'Journal entry not found!')
        return redirect('my-thoughts')
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Delete the thought
        thought.delete()
        # Add message for success
        messages.success(request, 'Journal entry deleted successfully!')
        # Redirect to the my thoughts page
        return redirect('my-thoughts')
        
    return render(request, 'journal/delete_thought.html')

# Create a view for profile_management
@login_required(login_url='login') # Add this decorator to the profile_management view preventing unauthorized access
def profile_management(request):
    # Create an instance of the ProfileManagementForm class
    form = ProfileManagementForm(instance=request.user)
    
    # Check if the form has been submitted
    if request.method == 'POST':
        # Create an instance of the ProfileManagementForm class with the data from the form
        form = ProfileManagementForm(request.POST, instance=request.user)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form
            form.save()
            # Add message for success
            messages.success(request, 'Profile updated successfully!')
            # Redirect to the profile management page
            return redirect('dashboard')
    
    # Create a dictionary to store the form
    context = {
        'form': form,
    }
    
    # Render the profile management page template
    return render(request, 'journal/profile_management.html', context)

# Create a view to delete a user account
@login_required(login_url='login') # Add this decorator to the delete_account view preventing unauthorized access
def delete_account(request):
    # Check if the request method is POST
    if request.method == 'POST':
        #delete the user
        request.user.delete() 
        # Add message for success and redirect to the home page
        messages.success(request, 'Account deleted successfully!')
        return redirect('')  # Redirect to a specific URL after deletion

    return render(request, 'journal/delete_account.html')



