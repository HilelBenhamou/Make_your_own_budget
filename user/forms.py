from django.forms import Form, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']