"""shaheedbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers                 
from media import views

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()                   
router.register(r'photo', views.PhotoView, 'photo')
router.register(r'animation', views.AnimationView, 'animation')
router.register(r'music', views.MusicView, 'music')
router.register(r'simulation', views.SimulationView, 'simulation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('media.urls')),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)