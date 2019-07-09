from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-board-home'),
    path('upload/', views.uploadPicture, name='main-board-upload'),
    path('image/<int:pk>', views.imageDetail, name='image-detail')
]