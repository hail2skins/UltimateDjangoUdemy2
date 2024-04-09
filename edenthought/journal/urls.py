from django.urls import path
# Import journal views
from . import views

# for change password do imports
from django.contrib.auth import views as auth_views

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
    # for change password
    # 1 - allow the user to enter their email address
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # 2 - email sent success message
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # 3 - link to password reset form in email
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # 4 - password successfully changed message
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
