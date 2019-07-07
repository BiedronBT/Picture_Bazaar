from django.shortcuts import render
from .models import Picture

# Create your views here.
def home(request):
    images = Picture.objects.all()
    return render(request, 'main_board/home.html', {'images': images})