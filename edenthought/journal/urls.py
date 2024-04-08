from django.urls import path
# Import journal views
from . import views

urlpatterns = [
    path('', views.home, name=''), # Home page path
    path('register/', views.register, name='register'), # User registration path
    path('login', views.login, name='login'), # User login path
    path('dashboard', views.dashboard, name='dashboard'), # User profile/dashboard path
    
]
