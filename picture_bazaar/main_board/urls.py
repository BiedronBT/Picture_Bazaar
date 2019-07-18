from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board'),
    path('<str:tag>', views.home, name='board-bytag'),
    path('uploaded/', views.uploaded_pictures, name='board-uploaded'),
    path('upload/', views.upload_picture, name='image-upload'),
    path('image/<int:pk>', views.image_detail, name='image-detail')
]