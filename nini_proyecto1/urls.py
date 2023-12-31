"""
URL configuration for nini_proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from nini_app1 import views as v1
from nini_app1 import views as v2
from nini_app2 import views as v3
from nini_app2 import views as v4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vista1/', v1.vistaUno),
    path('vista2/', v2.vistaDos),
    path('vista3/', v3.vistaTres),
    path('vista4/', v4.vistaCuatro),
]
