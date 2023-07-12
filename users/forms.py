from django.contrib.auth.forms import UserChangeForm, UserCreationForm, SetPasswordForm, PasswordResetForm
from django import forms
from django.utils.translation import gettext_lazy as _

from mailing.forms import FormStyleMixin
from users.models import User


class UserForm(FormStyleMixin, UserChangeForm):
    """Форма для профиля пользователя"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'middle_name', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserRegisterForm(FormStyleMixin, UserCreationForm):
    """Форма для регистрации пользователя"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class CustomPasswordResetForm(FormStyleMixin, PasswordResetForm):
    """Форма для сброса пароля"""
    email = forms.EmailField(
        label=_("Email"),
        max_length=50,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User


class PasswordResetConfirmForm(FormStyleMixin, SetPasswordForm):
    """Форма для обновления пароля"""
    class Meta:
        model = User
