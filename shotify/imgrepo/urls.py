from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # i.e. images/moe/
    path('<str:username>/', views.user_images, name='user_images'),
    # i.e. images/moe/3
    # TODO: change to slug
    path('<str:username>/<int:image_id>/', views.detail, name='detail')
]