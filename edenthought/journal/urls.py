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
    path('delete_thought/<str:pk>', views.delete_thought, name='delete_thought'), # Delete user thought path
    path('profile_management', views.profile_management, name='profile_management'), # User profile management path
    path('delete_account', views.delete_account, name='delete_account'), # Delete user account path
]
