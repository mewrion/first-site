"""mysite URL Configuration

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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
    path('' , include('blog.urls'))
=======
    path('', include('blog.urls')),
>>>>>>> a0da7fa2ade7f6601fba34d62649740e01b11e4e
=======
>>>>>>> feb3daeebdbd8b5e81ecaa5b408514e6dc5fa1ae
]
