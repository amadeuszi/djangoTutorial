"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog import settings
import cv.views
import plans.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cv.views.home, name='home'),
    path('fund/', cv.views.fund, name='fund'),
    path('diet/', cv.views.diet, name='diet'),
    path('up/', cv.views.up, name='up'),
    path('down/', cv.views.down, name='down'),
    path('schedule-add/', plans.views.schedule_add, name='schedule_add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
