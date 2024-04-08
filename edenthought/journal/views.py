from django.shortcuts import render
from django.shortcuts import redirect # Import redirect function from django

# Import forms model class for user creation
from .forms import CreateUserForm


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
            # Save the form
            form.save()
            # Redirect to the login page
            return redirect('login')
            
    # Create a dictionary to store the form
    context = {
        'form': form,
    }
    
    # Render the registration page template
    return render(request, 'journal/register.html', context)

# User login view
def login(request):
    
    # Render the login page template
    return render(request, 'journal/login.html')


# User profile/dashboard view
def dashboard(request):
    
    # Render the dashboard page template
    return render(request, 'journal/dashboard.html')

