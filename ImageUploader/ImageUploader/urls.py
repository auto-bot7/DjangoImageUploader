from django.conf import settings                          #import the below two packages to handle static media files
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #handling media url
   #print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))  - prints url pattern