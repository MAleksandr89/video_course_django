from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .form import UserRegistrationForm, UserUpdateForm, ProfileImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {
        'title': 'Страница регистрация',
        'form': form
    })

@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
            )
        updateUser = UserUpdateForm(
            request.POST,
            instance=request.user,
            )

        if profileForm.is_valid() and updateUser.is_valid():
            profileForm.save()
            updateUser.save()
            messages.success(request, f'Ваш профиль обновлен')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUser = UserUpdateForm(instance=request.user)

    data = {
        'profileForm': profileForm,
        'updateUser': updateUser
    }

    return render(request, 'users/profile.html', data)