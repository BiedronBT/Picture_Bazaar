from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Picture
from .forms import UploadPictureForm, EditPictureForm


def board(request):
    if request.user.is_authenticated:
        favorites = request.user.favorites.all()
    else:
        favorites = []

    # if tag:
    #     images = Picture.objects.filter(tags__icontains=tag).order_by('-date')[:20]
    #     header = f'Images with "{tag}" tag'
    #     return render(request, 'main_board/home.html', {'images': images, 'header': header, 'favorites': favorites})
    header = 'Most recent images'
    images = Picture.objects.all().order_by('-date')

    return render(request, 'main_board/home.html', {'images': images, 'header': header, 'favorites': favorites})


def filter_images(request):
    keyword = request.GET['q']
    header = f'Search results for "{keyword}"'
    images = Picture.objects.filter(title__icontains=keyword)
    return render(request, 'main_board/home.html', {'images': images, 'header': header})


def detail_image(request, picture_id):
    image = get_object_or_404(Picture, id=picture_id)
    tags = image.tags.split(',')
    return render(request, 'main_board/detail_image.html', {'image': image, 'tags': tags})


def upload_image(request):
    if request.method == 'POST':
        form = UploadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Image successfully uploaded!')
            return redirect('/')
    else:
        form = UploadPictureForm()
        return render(request, 'main_board/upload.html', {'form': form})


def edit_image(request, picture_id):
    if request.user == Picture.objects.get(id=picture_id).author:
        if request.method == 'POST':
            image = Picture.objects.get(id=picture_id)
            form = EditPictureForm(request.POST, instance=image)
            if form.is_valid():
                form.save()
                messages.success(request, 'Image updated')
                return redirect(reverse('detail-image', kwargs={'picture_id': picture_id}))
        else:
            form = EditPictureForm(instance=Picture.objects.get(id=picture_id))
            image = Picture.objects.get(id=picture_id)
            return render(request, 'main_board/edit_image.html', {'form': form, 'image': image})
    else:
        return redirect('/')


@login_required
def delete_image(request, picture_id):
    if request.user == Picture.objects.get(id=picture_id).author:
        if request.method == 'POST':
            image = Picture.objects.get(id=request.POST['image_id'])
            image.delete()
            profile_id = request.user.profile.id
            messages.success(request, 'Image has been deleted')
            return redirect(reverse('profile', kwargs={'profile_id': profile_id}))
        else:
            image = Picture.objects.get(id=picture_id)
            return render(request, 'main_board/delete_image.html', {'image': image})
    else:
        return redirect('/')


def mark_as_favorite(request, picture_id):
    if request.user.is_authenticated:
        image = get_object_or_404(Picture, id=picture_id)
        if image.favorites.filter(id=request.user.id):
            image.favorites.remove(request.user)
            return redirect(reverse('board'))
        else:
            image.favorites.add(request.user)
            return redirect(reverse('board'))
    else:
        messages.success(request, 'You need to be logged in to add images to favorites')
        return redirect(reverse('login'))