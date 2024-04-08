from django.shortcuts import render

# Create your views here.
# Create a view for the home page
def home(request):
    
    # Render the home page template
    return render(request, 'journal/index.html')

# User registration view
def register(request):
    
    # Render the registration page template
    return render(request, 'journal/register.html')

# User login view
def login(request):
    
    # Render the login page template
    return render(request, 'journal/login.html')


# User profile/dashboard view
def dashboard(request):
    
    # Render the dashboard page template
    return render(request, 'journal/dashboard.html')

