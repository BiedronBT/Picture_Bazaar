from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Picture
from .forms import UploadPictureForm


# Create your views here.
def home(request):

    images = Picture.objects.all()
    return render(request, 'main_board/home.html', {'images': images})


def imageDetail(request, pk):
    image = Picture.objects.filter(id=pk)
    print(image)
    return render(request, 'main_board/image_detail.html', {'images': image})


def uploadPicture(request):

    if request.method == 'POST':
        form = UploadPictureForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Image successfully uploaded!')
            return redirect('/')


    form = UploadPictureForm()
    return render(request, 'main_board/upload.html', {'form': form})