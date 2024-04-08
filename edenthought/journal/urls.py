from django.urls import path
# Import journal views
from . import views

urlpatterns = [
    path('', views.home, name=''), # Home page path
    path('register/', views.register, name='register'), # User registration path
    path('login', views.login, name='login'), # User login path
    path('dashboard', views.dashboard, name='dashboard'), # User profile/dashboard path
    path('logout', views.logout, name='logout'), # User logout path
    path('create-thought', views.create_thought, name='create-thought'), # Journal entry path
    path('my-thoughts', views.my_thoughts, name='my-thoughts'), # User thoughts path
    path('update_thought/<str:pk>', views.update_thought, name='update_thought'), # Update user thought path
]
