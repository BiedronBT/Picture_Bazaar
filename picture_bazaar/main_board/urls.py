from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-board-home'),
    path('uploaded/', views.uploaded_pictures, name='main-board-uploaded'),
    path('upload/', views.upload_picture, name='main-board-upload'),
    path('image/<int:pk>', views.image_detail, name='image-detail')
]