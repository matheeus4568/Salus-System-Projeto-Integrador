"""
URL configuration for SalusSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .m_views import *
from RequisicoesPacientes import urls as requisicoes_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste, name='teste'),
    path('teste/teste2/', teste, name='teste2'),
    path('teste/teste2/teste3/', teste, name='teste3'),
]


urlpatterns += requisicoes_urls.urlpatterns