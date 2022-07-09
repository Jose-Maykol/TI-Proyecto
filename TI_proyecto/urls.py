from django.contrib import admin
from django.urls import path, include
from homepage.views import HomeView
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', include('users.urls')),
    path('servicios/', include('servicios.urls')),
     path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
