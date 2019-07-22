from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('filter', views.filter_images, name='filter'),
    path('upload/', views.upload_image, name='upload-image'),
    path('edit_image/<int:picture_id>', views.edit_image, name='edit-image'),
    path('image/<int:picture_id>', views.detail_image, name='detail-image'),
    path('favorites/<int:picture_id>', views.mark_as_favorite, name='favorite-image'),
    path('<str:tag>', views.board, name='board-bytag'),
]
