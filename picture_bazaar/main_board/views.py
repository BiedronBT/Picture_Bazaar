from django.shortcuts import render, redirect
from .models import Picture
from .forms import UploadPictureForm


# Create your views here.
def home(request):
    images = Picture.objects.all()
    return render(request, 'main_board/home.html', {'images': images})



def uploadPicture(request):

    if request.method == 'POST':
        form = UploadPictureForm(request.POST, request.FILES)

        if form.is_valid():
            print(request.user)
            form.instance.author = request.user
            form.save()
            return redirect('/')


    form = UploadPictureForm(initial={'author': request.user})
    return render(request, 'main_board/upload.html', {'form': form})