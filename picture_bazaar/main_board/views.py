from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Picture, Favorite
from .forms import UploadPictureForm


def board(request, tag=None):
    if request.user.is_authenticated:
        favorites = [x.image for x in Favorite.objects.filter(user=request.user)]
    else:
        favorites = []

    if tag:
        images = Picture.objects.filter(tags__icontains=tag).order_by('-date')[:20]
        header = f'Images with "{tag}" tag'
        return render(request, 'main_board/home.html', {'images': images, 'header': header, 'favorites': favorites})
    else:
        header = 'Most recent images'
        images = Picture.objects.all().order_by('-date')[:20]
        return render(request, 'main_board/home.html', {'images': images, 'header': header, 'favorites': favorites})


def filter_images(request):
    keyword = request.GET['q']
    header = f'Search results for "{keyword}"'
    images = Picture.objects.filter(title__icontains=keyword)
    return render(request, 'main_board/home.html', {'images': images, 'header': header})


def detail_image(request, pk):
    image = get_object_or_404(Picture, id=pk)
    tags = image.tags.split(',')
    return render(request, 'main_board/image_detail.html', {'image': image, 'tags': tags})


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


def edit_image(request, picture=None):
    if request.method == 'GET':
        if request.user == Picture.objects.get(id=picture).author:
            form = UploadPictureForm(instance=Picture.objects.get(id=picture))
            return render(request, 'main_board/upload.html', {'form': form})
        else:
            return redirect('/')


def favorite_image(request, id=None):
    try:
        image = Favorite.objects.get(image__id=id)
        image.delete()
        return redirect(reverse('board'))
    except:
        image = Favorite.objects.create(user=request.user, image=Picture.objects.get(id=id))
        image.save()
        return redirect(reverse('board'))