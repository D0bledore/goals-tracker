from django.urls import path
from django.contrib.auth import views as auth_views
from . import forms
from . import views

app_name = 'accounts'


urlpatterns = [
        path('signup/', views.signup_view, name='signup'),
        path('login/', auth_views.LoginView.as_view(
            template_name='accounts/login.html',
            authentication_form=forms.CustomAuthenticationForm
            ), name='login'),
        path('logout/', auth_views.LogoutView.as_view(
            next_page='accounts:login'), name='logout'),
        path('profile/', views.profile_view, name='profile'),
        
        # Password change via profile
        path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
        path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
            template_name='accounts/password_change_done.html'), name='password_change_done'),

        # Password reset flow
        path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            form_class=forms.CustomPasswordResetForm), name='password_reset'),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            form_class=forms.CustomSetPasswordForm), name='password_reset_confirm'),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    ]

