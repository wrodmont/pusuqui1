from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academia/', include(('academia.urls', 'academia'), namespace='academia')), 
    path('alabanza/', include(('alabanza.urls', 'alabanza'), namespace='alabanza')),
    path('anfitriones/', include(('anfitriones.urls', 'anfitriones'), namespace='anfitriones')),
    path('cunakids/', include(('cunakids.urls', 'cunakids'), namespace='cunakids')),
    path('discipulado/', include(('discipulado.urls', 'discipulado'), namespace='discipulado')),
    path('encuentros/', include('encuentros.urls')),  # Si no usas namespace, puedes dejar así
    path('jap/', include('jap.urls')),
    path('multimedia/', include('multimedia.urls')),
    path('pusukids/', include(('pusukids.urls', 'pusukids'), namespace='pusukids')),
    path('account/', include('account.urls', namespace='account')),
    path('', home, name='home'),
]
