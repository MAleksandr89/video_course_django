from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите адрес электронной почты',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш адрес электронной почты'})
    )
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        help_text='Нельзя вводить @, /, _ и т.д.',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}))
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ваш пароль'}), 
        required=True,
        help_text='Пароль должен быть длиннее 8 символов')
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}),
        required=True)
    # some = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Адрес электронной почты',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш адрес электронной почты'})
    )
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        help_text='Нельзя вводить @, /, _ и т.д.',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput()
    )
    male = forms.ChoiceField(
        label='Пол',
        required=False,
        choices=[('male', 'Мужской'), ('female', 'Женский')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    email_send = forms.BooleanField(
        label='Подписатся на рассылку',
        required=False
    )
    class Meta:
        model = Profile
        fields = ['image', 'male', 'email_send']