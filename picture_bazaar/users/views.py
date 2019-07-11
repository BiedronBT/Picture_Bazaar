from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, EditUserForm, EditProfileForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('profile')

    user_form = EditUserForm(instance=request.user)
    profile_form = EditProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
