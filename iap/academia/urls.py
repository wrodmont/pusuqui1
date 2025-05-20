# academia/urls.py
from django.urls import path
from . import views

app_name = 'academia'  # Namespace para las URLs de esta aplicación

urlpatterns = [
    path('', views.index, name='index'),  # URL para la página principal de academia
    path('cursos/', views.cursos, name='cursos'),  # Ruta para la página de cursos
    # ... puedes agregar otras rutas aquí ...
]
