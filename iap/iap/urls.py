"""
URL configuration for iap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import render  # <--- importante: render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluir las URLs de las aplicaciones aquí:
    path('academia/', include('academia.urls')), 
    path('alabanza/', include('alabanza.urls')), # Ejemplo: Incluye las URLs de la aplicación 'app2'
    path('anfitriones/', include('anfitriones.urls')), # Ejemplo: Incluye las URLs de la aplicación 'app3'
    path('cunakids/', include('cunakids.urls')),
    path('discipulado/', include('discipulado.urls')),
    path('encuentros/', include('encuentros.urls')),
    path('jap/', include('jap.urls')),
    path('multimedia/', include('multimedia.urls')),
    path('pusukids/', include('pusukids.urls')),
    path('', home, name='home'),
    
]
