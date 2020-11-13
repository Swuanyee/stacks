from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'registrationInput',
                                                                         'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'registrationInput',
                                                                        'placeholder': 'Last Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'registrationInput',
                                                                     'placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'registrationInput',
                                                                            'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'registrationInput',
                                                                            'placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
