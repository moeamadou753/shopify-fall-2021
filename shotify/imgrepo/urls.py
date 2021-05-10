from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
    # i.e. images/moe/
    path('<str:username>/', views.user_images, name='user_images'),
    # i.e. images/moe/3
    # TODO: change to slug
    path('<str:username>/<int:image_id>/', views.detail, name='detail'),
    # i.e images/moe/3/delete
    path('<str:username>/<int:image_id>/delete', views.delete, name='delete_image')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
