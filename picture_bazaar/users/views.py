from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import UserRegisterForm, EditUserForm, EditProfileForm
from .models import Profile
from main_board.models import Picture

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


def profile(request, profile_id=None):
    if profile_id:
        profile = Profile.objects.get(id=profile_id)
        all_images = Picture.objects.filter(author=profile.user)

        paginator = Paginator(all_images, 8)
        try:
            page = request.GET['page']
        except:
            page = 1
        images = paginator.get_page(page)
        grid_style = 'equal'
        return render(request, 'users/profile.html', {'profile': profile, 'images': images, 'grid_style': grid_style})

    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('profile')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
        return render(request, 'users/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
