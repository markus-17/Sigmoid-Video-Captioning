from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo', views.demo, name='demo'),
    path('upload_video', views.upload_video, name='upload_video')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)