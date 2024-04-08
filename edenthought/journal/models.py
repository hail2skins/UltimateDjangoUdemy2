from django.db import models

# import auth user model
from django.contrib.auth.models import User # Allows us to use users to set auth 

# Create your models here.
# Create a model for the journal entry
class Thought(models.Model):
    # Create a field for the title
    title = models.CharField(max_length=150)
    # Create a field for the content
    content = models.TextField()
    # Create a field for the date
    date_posted = models.DateTimeField(auto_now_add=True)
    # Create a field for the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Create a string representation of the model
    def __str__(self):
        return self.title
