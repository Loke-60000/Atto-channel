from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Enter email', required=False, help_text= "(We don't check)", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "email"}))
    username = forms.CharField(label='Enter username', required=True, help_text="Prohibited characters: @, /, _", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "username"}))
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Enter password',
        required=True,
        help_text="Not less than 8 characters",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "password"})
        )
    password2 = forms.CharField(label='Confirm password', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "confirm password"}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Update email', required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "email"}))
    username = forms.CharField(label='Update username', required=True, help_text="Prohibited characters: @, /, _",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "username"}))
    # some = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['email', 'username']

