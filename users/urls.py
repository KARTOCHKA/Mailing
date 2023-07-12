from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView
from users.apps import UsersConfig
from users.views import ProfileUpdateView, RegisterView, EmailVerify, CustomPasswordResetView, \
    CustomPasswordResetConfirmView, CustomPasswordResetDoneView, CustomPasswordResetCompleteView

app_name = UsersConfig.name
urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password/reset/', CustomPasswordResetView.as_view(template_name='users/password_reset_form.html'),
         name='password_reset'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalid_verify'),
    path('password/reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password/reset/done', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete')
]
