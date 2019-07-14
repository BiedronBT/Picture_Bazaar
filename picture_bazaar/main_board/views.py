from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Picture
from .forms import UploadPictureForm


# Create your views here.
def home(request):

    images = Picture.objects.all()
    return render(request, 'main_board/home.html', {'images': images})


def uploaded_pictures(request):

    images = Picture.objects.filter(author=request.user)
    return render(request, 'main_board/home.html', {'images': images})


def image_detail(request, pk):

    image = get_object_or_404(Picture, id=pk)
    return render(request, 'main_board/image_detail.html', {'image': image})


def upload_picture(request):

    if request.method == 'POST':
        form = UploadPictureForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Image successfully uploaded!')
            return redirect('/')


    form = UploadPictureForm()
    return render(request, 'main_board/upload.html', {'form': form})