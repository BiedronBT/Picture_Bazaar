from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Picture
from .forms import UploadPictureForm


def board(request, tag=None):
    if tag:
        images = Picture.objects.filter(tags__icontains=tag).order_by('-date')[:20]
        header = f'Images with "{tag}" tag'
        return render(request, 'main_board/home.html', {'images': images, 'header': header})
    else:
        header = 'Most recent images'
        images = Picture.objects.all().order_by('-date')[:20]
        return render(request, 'main_board/home.html', {'images': images, 'header': header})

def filter_images(request):
    keyword = request.GET['q']
    header = f'Search results for "{keyword}"'
    images = Picture.objects.filter(title__icontains=keyword)
    return render(request, 'main_board/home.html', {'images': images, 'header': header})


def uploaded_pictures(request):
    images = Picture.objects.filter(author=request.user).order_by('-date')
    return render(request, 'main_board/home.html', {'images': images})


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